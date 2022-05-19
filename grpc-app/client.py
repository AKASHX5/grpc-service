import grpc
import meter_data_pb2, meter_data_pb2_grpc, data_service_pb2_grpc, data_service_pb2
import logging
from meter_data_pb2 import CreateDataRequest

_LOGGER = logging.getLogger(__name__)


def run():
    # with grpc.insecure_channel('localhost:50051') as channel:
    #     stub = meter_data_pb2_grpc.DataReprStub(channel)
    #     response = stub.show(meter_data_pb2.MeterUsage(meterReading = 15.80))
    #     # channel.close()
    # print("meter usage client received following from server: " + response.message)def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_service_pb2_grpc.DataStub(channel)
        print('stub', stub)
        try:
         response = stub.CreateData(CreateDataRequest(date='1/1/1'))
         print(response)
        except Exception as e:
            _LOGGER.exception("exception is ",str(e))

    # print("meter usage client received following from server: " + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()
