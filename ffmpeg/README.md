# Build docker image

`docker build --rm --tag ffmpeg .`

# Run container

1. `data` folder must contain:
- `pic.png` background picture
- `prm.json` subtitle styles
- `sub.ass` subtitles
- `snd.mp3` podcast audio

2. Run container via:
`docker run --rm -v $(pwd)/data:/opt/data ffmpeg`

3. Output filename is `out.mp4`
