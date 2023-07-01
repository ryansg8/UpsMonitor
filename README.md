# UPS Monitor

This Python script monitors the status of an Uninterruptible Power Supply (UPS) using the [NUT (Network UPS Tools)](https://networkupstools.org/) library. It sends a notification when the power is lost and when it is restored. The notifications are sent using [Pushbullet](https://www.pushbullet.com/), and an internet connection is required for sending the notifications.

## Prerequisites

Before running this script, ensure that you have the following prerequisites:

- Python 3.7 or later installed
- Docker installed (if using the provided Dockerfile)

## Installation

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, you need to configure the following variables in the `upsMonitor.py` file:

- `HOST`: The hostname or IP address of the NUT server.
- `UPS_NAME`: The name of the UPS device.
- `API_KEY`: The API key for Pushbullet.

## Usage

To run the script, execute the following command:

```shell
python upsMonitor.py
```

## Dockerization

Alternatively, you can use Docker to containerize the script. The provided Dockerfile sets up the necessary environment.

1. Build the Docker image using the following command:

   ```shell
   docker build -t ups-monitor .
   ```

2. Run the Docker container:

   ```shell
   docker run -d --name ups-monitor-container ups-monitor
   ```

   Make sure to replace `ups-monitor-container` with the desired container name.

## Notes

- The script continuously monitors the UPS status and sends a Pushbullet notification when the power is lost and restored.
- It uses multi-threading to send notifications asynchronously.
- An internet connection is required to send the notifications.
- The script assumes that the NUT server and the Pushbullet API are properly configured.

## License

This script is licensed under the [MIT License](LICENSE).