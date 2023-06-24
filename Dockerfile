FROM python:latest
WORKDIR /monitor_agent
COPY monitor_agent/ /monitor_agent/
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "influxdbAgent.py", "-t 4TnoobTtycEXt7JZCXKcLGuwvJv29osdsXd8fSQVabGsQ2yvuxCIvEIo0d7ylTgHDT-hbOhXo0fqZ628bsNgGw==", "-o MonitorAgent", "-b Measurements", "-u http://influxdb:8086", "--async" ]