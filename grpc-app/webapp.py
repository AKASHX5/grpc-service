import os
import json
from flask import Flask, render_template
import grpc
import logging
import datetime
from google.protobuf.json_format import MessageToJson

import data_service_pb2_grpc, data_service_pb2, meter_data_pb2_grpc, meter_data_pb2

app = Flask(__name__)

meter_host = os.getenv("METER_HOST", "localhost")
_LOGGER = logging.getLogger(__name__)

print(meter_host)


meter_channel = grpc.insecure_channel(
    f"{meter_host}:50051"
)

meter_client = data_service_pb2_grpc.DataStub(meter_channel)




@app.route("/")
def home():
    return render_template(
        "home.html"
    )





@app.route("/data")
def render_data():
    data_request = meter_data_pb2.CreateDataRequest(
        date=str(datetime.datetime.now())
    )
    _LOGGER.info(data_request)

    try:
        data_response = meter_client.CreateData(
            data_request
        )
        # print(data_response)
    except Exception as e:
        _LOGGER.error("error occured due to expetion" +str(e))

    data_json = (MessageToJson(data_response))
    # print(type(data_json))
    # _LOGGER.info("json data is: " +str(data_response))


    return render_template(
        "homepage.html", data=data_json
    ),201


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3001,debug=True,threaded=True)