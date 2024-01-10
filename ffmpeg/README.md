# Video generation for podcast

Input: `data` folder
Output: `out.mp4` video file

# Build docker image

`docker build --rm --tag ffmpeg .`

# Run container with ffmpeg to generate videofile

1. `data` folder must contain:
- `pic.png` background picture
- `prm.json` subtitle styles
- `sub.ass` subtitles
- `snd.mp3` podcast audio

2. Run container via:
`docker run --rm -v $(pwd)/data:/opt/data ffmpeg`

3. Output filename is `out.mp4`

# Run container with ffmpeg to mix in background music
1. Run container via:
`docker run --rm -v $(pwd)/<folder_with_episode>:/opt/data ffmpeg bash -c ""cd /opt/data; ../mixaudio.sh <episode_file_name>.mp3""

2. Output filename is `<episode_file_name>_music.mp3`
