
FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    pulseaudio \
    pulseaudio-utils && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "if [ -f setup_pulseaudio.sh ]; then chmod +x setup_pulseaudio.sh && ./setup_pulseaudio.sh; fi; if [ -f start ]; then bash start; elif [ -f start.sh ]; then bash start.sh; elif [ -f main.py ]; then python3 main.py; elif [ -f bot.py ]; then python3 bot.py; else echo 'Startup file not found'; ls -la; exit 1; fi"]
