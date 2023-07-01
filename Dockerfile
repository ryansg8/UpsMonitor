FROM python:3.7
WORKDIR /app
COPY upsMonitor.py /app/upsMonitor.py
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "upsMonitor.py"]