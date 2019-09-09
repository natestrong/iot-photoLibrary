FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install numpy
RUN git clone https://github.com/LibRaw/LibRaw.git libraw
    && git clone https://github.com/LibRaw/LibRaw-cmake.git libraw-cmake
    && cd libraw
    && git checkout 0.19.0
    && cp -R ../libraw-cmake/* .
    && cmake .
    && sudo make install
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
