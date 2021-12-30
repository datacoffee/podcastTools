# Build docker image

`docker build --rm --tag subgen .`

# Run container (data folder must contain snd.mp3)

`docker run --rm -v $(pwd)/data:/opt/data subgen`