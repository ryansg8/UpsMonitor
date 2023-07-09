import logging
from threading import Thread
from time import time
from urllib import request

from nut2 import PyNUTClient
from pushbullet import PushBullet

# CONFIGURE HOST, UPS_NAME, AND API_KEY 
HOST = ""
UPS_NAME = ""
API_KEY = ""

# CONSTANTS
STATUS = "ups.status"
DISCHARGE = "OB DISCHRG"

def main():
    logging.info("Running....")
    client = PyNUTClient(host=HOST)
    vars = client.list_vars(UPS_NAME)
    status = vars[STATUS]
    if (status == DISCHARGE):
        onPowerloss(client)
    else:
        onPower(client)

def onPower(client, elapsed_time = None):
    logging.info("UPS is connected to power")
    
    # If we recovered from powerloss, send a notification.
    if (elapsed_time):
        logging.info(f"Power recovered after {elapsed_time} minutes")
        thread = Thread(target=sendPushBullet(elapsed_time))
        thread.start()

    vars = client.list_vars(UPS_NAME)
    status = vars[STATUS]
    while status != DISCHARGE:
        vars = client.list_vars(UPS_NAME)
        status = vars[STATUS]
    onPowerloss(client)


def onPowerloss(client):
    start_time = time()
    logging.info("UPS is disconnected from power")
    vars = client.list_vars(UPS_NAME)
    status = vars[STATUS]
    while status == DISCHARGE:
        vars = client.list_vars(UPS_NAME)
        status = vars[STATUS]
    end_time = time()
    onPower(client, elapsed_time = round(((end_time - start_time) / 60), 2))

def checkInternetConnection():
    try:
        request.urlopen('http://www.google.com', timeout=1)
        return True
    except request.URLError:
        return False
    
def sendPushBullet(elapsed_time):
    pb = PushBullet(API_KEY)
    interentConnected = checkInternetConnection()


    while (interentConnected != True):
        interentConnected = checkInternetConnection()
    
    logging.info("Sending pushbullet...")
    pb.push_note("Power loss!", f"Power was lost for {elapsed_time} minutes, but has now been restored!")
    return


if __name__ == "__main__":
    main()