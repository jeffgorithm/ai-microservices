import os

from flask import Flask, render_template, request
import grpc

from wine_quality_pb2 import WineQualityRequest
from wine_quality_pb2_grpc import WineQualityStub

app = Flask(__name__)

wine_quality_host = os.getenv("WINE_QUALITY_HOST", "localhost")
wine_quality_channel = grpc.insecure_channel(f"{wine_quality_host}:50051")
wine_quality_client = WineQualityStub(wine_quality_channel)

@app.route("/")
def render_homepage():
    fixed_acidity = request.args.get("fixed_acidity", "")
    volatile_acidity = request.args.get("volatile_acidity", "")
    citric_acidity = request.args.get("citric_acidity", "")
    alcohol = request.args.get("alcohol", "")
    if fixed_acidity and volatile_acidity  and citric_acidity and alcohol:
        wine_quality_request = WineQualityRequest(fixed_acidity=float(fixed_acidity), volatile_acidity=float(volatile_acidity), 
                                                  citric_acidity=float(citric_acidity), alcohol=float(alcohol))
        print(wine_quality_request)
        wine_quality_response = wine_quality_client.wine_quality(wine_quality_request)
        return render_template("homepage.html",wine_quality=wine_quality_response.wine_quality)
    else:
        return render_template("homepage.html",wine_quality='')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
