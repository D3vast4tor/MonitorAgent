# MonitorAgent

## Version: 1.0

### A monitoring agent for containers running in your machine

### This software was build using InfluxDB, Grafana and a modified version of [Cestnut](https://github.com/Cestnut/DockerResourcesDisplayer-Container)'s script

In the **dashboard** folder there's a json file to import a basic Grafana dashboard with rows, visualizations and query's code.

#### Configuration

To make sure that the MonitorAgent can send data about resource usage to InfluxDB you have to configure it first.

Delete and edit the lines:`YOUR_TOKEN`,`YOUR_ORG`,`YOUR_BUCKET` and eventually the default username and password that are both `admin`.

Also edit the arguments in the docker file accordingly to the precedent step, if you want to know all the arguments avaiable for the python file simply run `python3 influxdbAgent.py --help` in a virtual enviroment such as Conda, venv or similar. Specify the request method in the url such as `http://address:port`

Simply run `docker compose up` to start building the images and containers required.

After that you should see a log for the 3 main containers: **StorageAgent**, **DisplayerAgent** and **MonitorAgent**.

Additionally you have to set up a datasource for Grafana, simply access the webpage at the url `localhost:3000`, follow the guided steps to modify default password if you want, then click on **Add your first data source**

Select InfluxDB and set everything according to how you have choose in the previous steps.

Pay attention to the url that need to be set to `http://influxdb:8086`.

After that you can create a dashboard or import a json file like the one under the **dashboard** folder.
