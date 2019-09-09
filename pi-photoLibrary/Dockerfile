FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install numpy

RUN apt-get install libraw-dev

#RUN git clone https://github.com/LibRaw/LibRaw.git libraw
#RUN git clone https://github.com/LibRaw/LibRaw-cmake.git libraw-cmake
#RUN cd libraw
#RUN git checkout 0.19.0
#RUN cp -R ../libraw-cmake/* .
#RUN cmake .
#RUN sudo make install

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
