### mp3Shownotes2Md
Tooling for exporting show notes (stored in id3 tag of mp3 file) to markdown file


### processReaperMarkers
Tooling for adding chapters to mp3 ID3 tags

#### Docker

Build image:

$ docker build --tag chapters .

Add chapters to mp3 file (file should be **snd.mp3**):

$ docker run --rm -v $(pwd):/opt/data chapters