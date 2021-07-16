ARG ARCH=
FROM docker.io/library/python:3.7.3-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["/app/gunicorn.sh"]
