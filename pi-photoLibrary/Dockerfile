FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip install numpy

# libraw ########
RUN mkdir /tmp/deps
RUN cd /tmp/deps
RUN curl -X GET https://www.libraw.org/data/LibRaw-0.19.0.tar.gz > libraw.tar.gz
RUN tar -zxf libraw.tar.gz
RUN cd LibRaw-0.19.0/
RUN ./configure
RUN make -j 6
RUN make install

RUN pip install rawpy --no-binary rawpy

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
