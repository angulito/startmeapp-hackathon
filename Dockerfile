FROM python:3.7.1-stretch

RUN apt-get update && apt-get install -y \
    curl \
    libssl-dev \
    htop \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

# flask default port
EXPOSE 5000

CMD ["gunicorn", "--config", "/usr/app/gunicorn_config.py", \
                 "--pythonpath", "/usr/app/src", \
                 "--preload", "-k", "gevent", "src.main:APP"]