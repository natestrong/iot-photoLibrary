#FROM python:3
#WORKDIR /usr/src/app
#COPY requirements.txt .
#
#RUN pip install numpy
#
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
#CMD ["python", "app.py"]

FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .

RUN apt-get install exiftool -y
RUN apt-get install python3-pil -y
RUN apt-get install ffmpeg -y

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
