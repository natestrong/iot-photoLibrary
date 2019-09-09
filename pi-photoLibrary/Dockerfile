FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip install numpy

# libraw ########
RUN
    cd /tmp/deps && \
    curl -X GET https://www.libraw.org/data/LibRaw-0.19.0.tar.gz > libraw.tar.gz && \
    tar -zxf libraw.tar.gz && \
    cd LibRaw-0.19.0/ && \
    ./configure && \
    make -j 6 && \
    make install && \

RUN pip install rawpy --no-binary rawpy

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
