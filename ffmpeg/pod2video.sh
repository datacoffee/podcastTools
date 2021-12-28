#!/bin/sh

figlet "Make Video..."
ffmpeg -y -r 1/5 -loop 1 -i /opt/data/pic.png -i /opt/data/snd.mp3 -shortest -c:v libx264 -vf "fps=1,format=yuv420p,subtitles=/opt/data/sub.ass" -s 3840x2160 -c:a copy /opt/data/out.mp4
figlet "Done!"
