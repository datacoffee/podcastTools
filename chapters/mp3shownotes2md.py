import argparse
import os

from mutagen.id3 import ID3, CHAP


def get_hms_timecode(value: CHAP) -> str:
    time_code: int = value.start_time

    seconds = (time_code / 1000) % 60
    seconds = int(seconds)
    minutes = (time_code / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (time_code / (1000 * 60 * 60)) % 24
    hours = int(hours)

    minutes_str: str = str(minutes)
    seconds_str: str = str(seconds)
    if len(seconds_str) == 1:
        seconds_str = "0" + seconds_str
    hours_str: str = ""

    time_code_str: str = minutes_str + ":" + seconds_str
    if hours > 0:
        hours_str = str(hours) + ":" + time_code_str

    return time_code_str


def print_shownotes_as_md(path_to_mp3_file: str):
    audio: ID3 = ID3(path_to_mp3_file)
    shownotes_path: str = path_to_mp3_file + ".md"
    with open(shownotes_path, "w") as f:
        f.write(f"# Data Coffee podcast{os.linesep}")
        f.write(f"## {audio.get('TIT2', '')}{os.linesep}{os.linesep}")
        f.write(f"Shownotes: {os.linesep}")

        for key, value in audio.items():
            if "CHAP" in key:   
                f.write(f"{os.linesep}- {get_hms_timecode(value)} {value.sub_frames['TIT2']}")
                if 'WXXX:chapter url' in value.sub_frames:
                    f.write(f"{os.linesep} {value.sub_frames['WXXX:chapter url'].url}")
                f.write(os.linesep)

    print(f"[DONE] Exported shownotes to {shownotes_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MP3 shownotes exports to markdown')
    parser.add_argument('--mp3', type=str, help="Input mp3 file", required=True)
    kwargs = vars(parser.parse_args())
    print_shownotes_as_md(kwargs['mp3'])
