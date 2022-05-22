from concurrent import futures
import random
import time
import grpc

import data_service_pb2 as datamessage
import data_service_pb2_grpc as dataservice
import meter_data_pb2 as meterdata
import meter_data_pb2_grpc as meterservice
_ONE_DAY_IN_SECONDS = 60 * 60 * 24






class MeterService(dataservice.DataServicer):
    def CreateData(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        print("got request: " + str(request))

        print(request.date)
        data = meterdata.MeterData(date=request.date, meterusage=12.2)
        print(data)
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
