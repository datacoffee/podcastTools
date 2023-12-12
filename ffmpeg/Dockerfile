FROM ubuntu:20.04

RUN apt-get -y update
RUN apt-get install -y ffmpeg
RUN apt-get install -y figlet

COPY pod2video.sh /opt/
COPY mixaudio.sh /opt/

# could be sh script
CMD ["/opt/pod2video.sh"]
