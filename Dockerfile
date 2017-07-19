FROM registry.aliyuncs.com/slzcc/python:3
RUN git clone -b scrapy_redis https://github.com/slzcc/Scrapy-DangDang.git && \
    cd Scrapy-DangDang && \
    pip install -r package.txt

ENV REDIS_HOST=127.0.0.1 \
    REDIS_PORT=6379 \
    CONCURRENT_REQUESTS=32 \
    DOWNLOAD_DELAY=1

WORKDIR /Scrapy-DangDang

CMD ["python", "main.py"]

