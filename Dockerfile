FROM linuxserver/calibre:latest

WORKDIR /HinaSenei

RUN apt-get -y update \
  && apt -y install python3-pip \
  && apt-get update -qq && apt-get -y install ffmpeg \
  && pip3 install pyrogram \
  && pip3 install tgcrypto \
  && pip3 install python-dotenv 
  
COPY . .

CMD ["bash","start.sh"]