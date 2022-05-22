import os
import json
from flask import Flask, render_template
import grpc
import datetime
from google.protobuf.json_format import MessageToJson

import data_service_pb2_grpc, data_service_pb2, meter_data_pb2_grpc, meter_data_pb2

app = Flask(__name__)

meter_host = os.getenv("METER_HOST", "localhost")
print(meter_host)


meter_channel = grpc.insecure_channel(
    f"{meter_host}:50051"
)

meter_client = data_service_pb2_grpc.DataStub(meter_channel)

@app.route("/data")
def render_homepage():
    data_request = meter_data_pb2.CreateDataRequest(
        date=str(datetime.datetime.now())
    )
    print(data_request)

    # try:
    data_response = meter_client.CreateData(
        data_request
    )
    print(MessageToJson(data_response))
    # except Exception as e:
    #     print("failed due to " +str(e))

    data_json = (MessageToJson(data_response))

    return render_template(
        "homepage.html", data=data_json
    ),201


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3001,debug=True,threaded=True)