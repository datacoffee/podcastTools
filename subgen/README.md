# subgen
Generate subs file from mp3 file
Input: folder `data` with 2 files, `snd.mp3` (your podcast mp3 file) and `prm.json` (settings)
Output: file `sub.ass`

# Build docker image

`docker build --rm --tag subgen .`

# Run container (data folder must contain snd.mp3)

`docker run --rm -v $(pwd)/data:/opt/data subgen`