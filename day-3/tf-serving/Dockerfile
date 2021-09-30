FROM ubuntu:latest

# Install tensor-flow-server
RUN apt -y update && apt -y upgrade
RUN apt-get -y install curl
RUN apt install -y python3-pip
RUN pip install -U setuptools
RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
RUN apt-get update && apt-get install tensorflow-model-server
RUN apt-get upgrade tensorflow-model-server

COPY models/ /models/

CMD ["tensorflow_model_server", "--port=8500", "--rest_api_port=8501", "--model_name=model", "--model_base_path=/models/model"]
