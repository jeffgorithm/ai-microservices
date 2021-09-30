import grpc
from wine_quality_pb2_grpc import WineQualityStub
from wine_quality_pb2 import WineQualityRequest
channel = grpc.insecure_channel("localhost:50051")
client = WineQualityStub(channel)
request = WineQualityRequest()
client.wine_quality(request)
request = WineQualityRequest(fixed_acidity = 7.0, volatile_acidity = 0.3, citric_acidity=1.3, alcohol=9.0)
print(client.wine_quality(request))

