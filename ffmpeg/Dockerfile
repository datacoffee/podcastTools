FROM ubuntu:20.04

# Update and install necessary packages
RUN apt-get -y update && \
    apt-get install -y ffmpeg figlet fonts-comfortaa && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a new user and switch to that user
RUN useradd -m myuser
USER myuser
COPY mixaudio.sh /opt/
COPY background.mp3 /opt/

# Copy the script to the docker image
COPY --chown=myuser:myuser pod2video.sh /opt/

# Set the script as the command to be run
CMD ["/opt/pod2video.sh"]