# Podcast tools
This repo keeps tracks of the tools and toolchains used to prepare Data Coffee podcast (mp3 files, shownotes and other artifacts).

## Audio -> video pipeline

- create your audio as mp3 file *with chapters* integrated as metadata into the file
- run `subgen`: it takes `snd.mp3` and `prm.json` as input -> generates `sub.ass` as output
- run `ffmpeg`: it takes `snd.mp3` and `sub.ass` as input -> generates `out.mp3` as output

## New audio->video pipeline

## References
- https://www.editframe.com/guides/how-to-add-an-audio-waveform-or-visualizer-to-a-video-using-ffmpeg
- https://christianheilmann.com/2023/08/31/adding-sound-wave-overlays-to-videos-and-pictures-using-ffmpeg/