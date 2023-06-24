FROM python:latest
WORKDIR /monitor_agent
COPY monitor_agent/ /monitor_agent/
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "influxdbAgent.py", "-t TOKEN", "-o ORG", "-b BUCKET", "-u URL" ]