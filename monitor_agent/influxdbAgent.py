from influxdb_client.client.write_api import SYNCHRONOUS,ASYNCHRONOUS
from collect_stats import *
from influxdb_client import WriteApi,InfluxDBClient, Point, WritePrecision
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
import argparse
###########################################################################################
# DEFINITION OF FUNCTIONS TO PERIODICALLY INSERT VALUE TO INFLUXDB WITH A PSEUDO-OVERLOAD #
#                   FOR TIMER ARGUMENT TO CHOOSE THE PREFERRED INTERVAL                   #
###########################################################################################
def write_data(writer_api: WriteApi,containers_stats: dict,bucket: str,org: str,timer= 1):
        for container in containers_stats:
            name = containers_stats[container]['name']
            cpu = containers_stats[container]['cpu']
            memory = containers_stats[container]['memory']
            net_in = containers_stats[container]['network_in']
            net_out = containers_stats[container]['network_out']
            #DECOMPUTE CONTAINER STATS#
            p = (
                Point(name)
                #("cpu",cpu)
                .field("cpu",cpu)
                .tag("cpu",cpu)
                #("memory",memory)
                .field("memory",memory)
                .tag("memory",memory)
                #("network_in",net_in)
                .field("network_in",net_in)
                .tag("network_in",net_in)
                #("network_out",net_out)
                .field("network_out",net_out)
                .tag("network_out",net_out)
            )
            writer_api.write(bucket,org,record=p)
        time.sleep(timer)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-t",
                    "--token",
                    required=True,
                    help="Specify the token to access InfluxDB by the script.")
    ap.add_argument("-o",
                    "--org",
                    required=True,
                    help="Specify the InfluxDB organization for query execution.")
    ap.add_argument("-b",
                    "--bucket",
                    help="Optional, specify the default bucket to look for when sending data.")
    ap.add_argument("-u",
                    "--url",
                    required=True,
                    help="Specify the url to interrogate when performing a query.\n")
    ap.add_argument("-a",
                    "--async",
                    const=True,
                    nargs='?',
                    help="Specify to write an async query for every container.\nBy default the query will be synchronous.")
    args = vars(ap.parse_args())
    ############################
    # RETRIEVING THE ARGUMENTS #
    ############################
    org = args['org'].replace(" ","")
    bucket = args['bucket'].replace(" ","")
    url = args['url'].replace(" ","")
    token = args['token'].replace(" ","")
    #############################################################################################################################
    #            CREATING THE CLIENT OBJECT TO COMMUNICATE WITH INFLUXDB AND A WRITER TO STORE DATA INTO INFLUXDB               #
    #############################################################################################################################
    client = InfluxDBClient(url,token,org)
    
    if (args['async'] == None):
        while True:
            writer = client.write_api(write_options=SYNCHRONOUS)
            write_data(writer_api=writer,containers_stats=all_containers_stats(),bucket=bucket,org=org,timer=0.5)
    else:
        while True:
            writer = client.write_api(write_options=ASYNCHRONOUS)
            write_data(writer_api=writer,containers_stats=all_containers_stats(),org=org,bucket=bucket)
        
if __name__ == "__main__":
    main()

