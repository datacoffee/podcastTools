#!/usr/bin/env python

import json
import time
from eyed3.id3 import Tag

with open('/opt/data/prm.json', 'r') as prmfile:
    prmdata = prmfile.read()

# parse file
params = json.loads(prmdata)

# construct subtitles header
subtitles = f"""[Script Info]
ScriptType: v4.00
Collisions: Normal
; screen resolution, of the author of this file.
PlayResX: {params["Script Info"]["ResX"]}
PlayResY: {params["Script Info"]["ResY"]}
PlayDepth: 0
; play at 100% speed.
Timer: 100,0000

; For further info on all these fields, refer to the document
; "Sub Station Alpha v4.00+ Script Format"

[V4 Styles]
; this line is actually ignored by the parser, but I include it for improving readability.
Format: {params["V4 Styles"]["Format"]}
; 153 specifies the red RGB color 0x000099. Note that the order is 0xBBGGRR.
; and note that 153 is the value of 0x000099, in base 10.
; 6 specifies the alignment of the text.
; for centered alignment, we specify 2. To then move it to the top, we add 4.
; so we end up with 2 + 4 = 6
Style: Topic,{params["V4 Styles"]["Styles"]["Topic"]}
Style: Title,{params["V4 Styles"]["Styles"]["Title"]}

[Events]
Format: Marked, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# read chapters from mp3 file
tag = Tag()
tag.parse("/opt/data/snd.mp3")
chapters = [
    {
        "Start": "0:00:00.00",
        "End": "5:00:00.00",
        "Style": "Title",
        "Text": tag.title
    }
]

print(tag.artist)
print(tag.title)

header_html = """<p><strong>Ведущие подкаста 'Data Coffee' обсуждают новости и делятся своими мыслями!</strong></p>
<p><br></p>
<p>Shownotes:</p>\n"""
footer_html = """<p><br></p>
<p>Сайт: <a href='https://datacoffee.link/'>https://datacoffee.link</a></p>
<p>Telegram: <a href='https://t.me/datacoffee'>https://t.me/datacoffee</a></p>
<p>Mastodon: <a href='https://techhub.social/@datacoffee'>https://techhub.social/@datacoffee</a></p>
<p>Чат подкаста: <a href='https://t.me/datacoffee_chat'>https://t.me/datacoffee_chat</a></p>"""
chapters_html = ""

for chapter in tag.chapters:
    new_chapter = {}
    new_chapter["Style"] = "Topic"
    new_chapter["Start"] = time.strftime('%-H:%M:%S.00', time.gmtime(chapter.times[0] / 1000))
    new_chapter["End"] = time.strftime('%-H:%M:%S.00', time.gmtime(chapter.times[1] / 1000))
    new_chapter["Text"] = chapter.sub_frames.get(b"TIT2")[0]._text
    chapters.append(new_chapter)

    if int(time.strftime('%-H', time.gmtime(chapter.times[0] / 1000))) > 0:
        chapter_time = time.strftime('%-H:%M:%S', time.gmtime(chapter.times[0] / 1000))
    else:
        chapter_time = time.strftime('%-M:%S', time.gmtime(chapter.times[0] / 1000))

    url_tag = chapter.sub_frames.get(b"WXXX")
    if url_tag and len(url_tag) > 0:
        chapters_html += f"""<p>{chapter_time} <a href='{url_tag[0].url}'>{new_chapter['Text']}</a></p>\n"""
    else:
        chapters_html += f"""<p>{chapter_time} {new_chapter['Text']}</p>\n"""

print(header_html, chapters_html, footer_html, sep='')

# construct events section
for chapter in chapters:
    subtitles += f'Dialogue: Marked=0,{chapter["Start"]},{chapter["End"]},{chapter["Style"]},,0000,0000,0000,,{chapter["Text"]}\n'

with open('/opt/data/sub.ass', 'w') as subfile:
    subfile.write(subtitles)
