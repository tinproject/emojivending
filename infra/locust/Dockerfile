FROM python:3.8

WORKDIR /opt/app

COPY requirements.txt /opt/app
COPY generate_traffic.py /opt/app

RUN pip install -r requirements.txt

EXPOSE 8089
