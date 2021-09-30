FROM tensorflow/tensorflow
WORKDIR /pipeline
COPY requirements.txt /pipeline
RUN pip install -r requirements.txt
COPY neural_network.py /pipeline