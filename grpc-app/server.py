from concurrent import futures
import random
import time
import grpc
import json
import csv

import logging
import data_service_pb2_grpc as dataservice
import meter_data_pb2 as meterdata
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


_LOGGER = logging.getLogger(__name__)


csvfilepath = "/Users/akash/PycharmProjects/MicroService/grpc-service/meterusage.csv"
jsonfilepath = "/Users/akash/PycharmProjects/MicroService/grpc-service/meterusage.json"

with open(csvfilepath, 'r') as csvf:
    csvReader = csv.reader(csvf)
    next(csvReader)
    data = {"meterusage": []}
    for rows in csvReader:
        data["meterusage"].append({"time": rows[0], 'meterusage': rows[1]})

with open(jsonfilepath, 'w') as f:
    json.dump(data, f, indent=4)

with open(jsonfilepath, 'rb') as readfile:
    data = json.load(readfile)
response = json.dumps(data, indent=4)



class MeterService(dataservice.DataServicer):


    def CreateData(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        try:
            data = meterdata.MeterData(date=request.date, meterusage=response)
            _LOGGER.info(data)
        except Exception as e:
            _LOGGER.info("No data due to exception", str(e))
        return meterdata.GetDataResult(meterdata=data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dataservice.add_DataServicer_to_server(MeterService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    print("server starting")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
