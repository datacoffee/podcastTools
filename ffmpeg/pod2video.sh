#!/bin/sh

figlet "Make Video..."
#ffmpeg \
#  -y -r 1/5 -loop 1 \
#  -i /opt/data/pic.png \
#  -i /opt/data/snd.mp3 \
#  -shortest -c:v \
#  libx264 -vf "fps=1,format=yuv420p,subtitles=/opt/data/sub.ass" \
#  -s 3840x2160 \
#  -c:a copy /opt/data/out.mp4


ffmpeg \
  -y -r 1/5 -loop 1 \
  -i /opt/data/pic.png \
  -i /opt/data/snd.mp3 \
  -shortest -c:v libx264 -preset fast \
  -vf "fps=1,format=yuv420p,subtitles=/opt/data/sub.ass" \
  -s 1280x720 \
  -c:a copy /opt/data/out.mp4


# ffmpeg -y -i /opt/data/pic.png -i /opt/data/snd.mp3 -filter_complex "[1:a]showwaves=s=400x200:mode=cline:colors=white@0.4,fps=25,format=yuva420p[wf];[0:v]scale=3840x2160,setsar=1,format=yuv420p[v];[v][wf]overlay=W-w-10:H-h-10:format=auto,subtitles=/opt/data/sub.ass" -shortest -c:v libx264 -c:a copy /opt/data/out.mp4

figlet "Done!"
