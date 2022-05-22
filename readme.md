After loosing a lot of sleep trying to get a basic example for repeated fields working, I finally got it.

The problem:

Create a calculator.py with two functions, square and multiplier.
Using GRPC, create a Proto file for the same.
Write a server, a client.
Run the server, and run the client to get correct results.
The Proto file:

syntax = "proto3";

message Number {
    int32 value = 1;
}

message NumList {
    string name = 1;
    repeated Number nums = 2;
}

service Calculator {
    rpc Multiplier(NumList) returns (Number) {}
    rpc Square(Number) returns (Number) {}
}
Now the square part is easy, but for the Multiplier, I wanted to pass a list of Numbers (as in Number type as defined in the proto file).

The problem was with the repeated field. And here is the ultimate solution in short.

The solution:

import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc
# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)
num_list = calculator_pb2.NumList()
num_list.name = 'MyFirstList'
n1 = num_list.nums.add()
n2 = num_list.nums.add()
n3 = num_list.nums.add()
n1.value = 10
n2.value = 20
n3.value = 30

assert len(num_list.nums) == 3

response = stub.Multiplier(num_list)
print(response.value)
The Calculator Multiplier function (because this needs to be shown):

def multiplier(numlist, name):
    mul = 1
    for num in numlist:
        mul = mul * num.value
    print(f'Result of list {name}')
    return mul
Hope this helps someone. Hope this is as descriptive as it should be.