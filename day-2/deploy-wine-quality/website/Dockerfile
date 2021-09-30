FROM python

RUN mkdir /service

COPY protobufs/ /service/protobufs/
COPY website/ /service/website/

WORKDIR /service/website

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=./ --grpc_python_out=. ../protobufs/wine_quality.proto

EXPOSE 8080

ENTRYPOINT [ "python", "website.py"]