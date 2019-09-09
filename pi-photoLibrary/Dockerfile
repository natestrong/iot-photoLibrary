#FROM python:3
#WORKDIR /usr/src/app
#COPY requirements.txt .
#
#RUN pip install numpy
#
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
#CMD ["python", "app.py"]

FROM ubuntu
WORKDIR /usr/src/app
COPY requirements.txt .

RUN apt update
RUN apt install python3-pip
RUN apt install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.7

RUN pip3 install numpy
RUN pip3 install rawpy

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3.7", "app.py"]
