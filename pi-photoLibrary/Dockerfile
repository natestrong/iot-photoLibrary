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
RUN apt install python3-pip -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.7 -y
RUN apt install exiftool -y
RUN apt install python3-pil -y

RUN apt install ffmpeg -y

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
