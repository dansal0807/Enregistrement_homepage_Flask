FROM alpine:3.7
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

ENTRYPOINT  ["python3"]

CMD ["app.py"]
