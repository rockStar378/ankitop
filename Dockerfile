
FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "if [ -f start ]; then bash start; elif [ -f start.sh ]; then bash start.sh; elif [ -f main.py ]; then python3 main.py; elif [ -f bot.py ]; then python3 bot.py; else echo 'ERROR: Startup file not found'; ls -la; exit 1; fi"]
