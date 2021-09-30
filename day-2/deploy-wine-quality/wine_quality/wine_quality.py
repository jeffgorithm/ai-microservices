from concurrent import futures

import grpc

from wine_quality_pb2 import WineQualityResponse
import wine_quality_pb2_grpc

# Load the model from file model.pkl
import pickle
file = open("model.pkl", "rb")
objs = pickle.load(file)
scaler = objs[0]
model = objs[1]

# class that implements the microservice functions
class WineQualityService(wine_quality_pb2_grpc.WineQualityServicer):
    def wine_quality(self, request, context):
        # Read inputs from request and rescale the variables
        input = [[request.fixed_acidity, request.volatile_acidity, 
        request.citric_acidity, request.alcohol]]
        input = scaler.transform(input)
        
        # Return wine quality based on the model
        pred = model.predict(input)[0]
        return WineQualityResponse(wine_quality=pred)


# create the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wine_quality_pb2_grpc.add_WineQualityServicer_to_server(WineQualityService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
