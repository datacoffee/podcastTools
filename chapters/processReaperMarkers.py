import argparse
import csv
import os
from pathlib import Path
import mp3chaps
from eyed3.id3 import Tag


class ChaptersProcessor:

    def __init__(self, mp3_file_path: str, reaper_marker_csv_path: str) -> None:
        super().__init__()
        self.mp3_file_path = mp3_file_path
        self.reaper_marker_csv_path = reaper_marker_csv_path

    def convert_reaper_markers_to_mp3chap(self) -> str:
        # mp3chap expects the file with content like
        #             00:00:00.000 Introduction
        #             00:02:00.000 Chapter Title
        #             00:42:24.123 Chapter Title
        #
        # It also expects file.mp3 and file.chapters.txt together
        mp3_chapters_file_path: str = str(
            Path(self.mp3_file_path).parent / Path(self.mp3_file_path).stem) + ".chapters.txt"
        with open(self.reaper_marker_csv_path, mode='r') as csv_file, \
                open(mp3_chapters_file_path, mode='w') as mp3_chap_file:
            reader = csv.DictReader(csv_file, delimiter=',', )
            for row in reader:
                time_stamp_original: str = row['Start']
                time_splits = time_stamp_original.split(":")
                hours, minutes, seconds, mss = time_splits[0], time_splits[1], time_splits[2], time_splits[3]
                time_stamp = "0" + hours + ":" + minutes + ":" + seconds + "." + mss + "0"
                chapter_name: str = str(row['Name']).capitalize()
                print(f"{time_stamp} {chapter_name}")
                mp3_chap_file.write(f"{time_stamp} {chapter_name} {os.linesep}")
        print(f"written chapters to {mp3_chapters_file_path}")
        return mp3_chapters_file_path

    def add_chapters_to_mp3_file(self):
        tag: Tag = Tag()
        tag.parse(str(self.mp3_file_path))
        print(f"")
        if tag.chapters:
            print("existing chapters:")
            mp3chaps.list_chaps(tag)
        mp3chaps.add_chapters(tag, self.mp3_file_path)


def cli_parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser(
        description='Tool gets csv export of time markers from Reaper '
                    'and mp3 file and writes markers as chapters to the mp3 file',
        formatter_class=argparse.RawTextHelpFormatter)

    _parser.add_argument('--mp3', type=str, help="Input mp3 file")
    _parser.add_argument('--chap', type=str, help="Csv file with exported markers from Reaper")
    return _parser


def validate_input_arguments(input_arguments: dict) -> dict:
    for key in ("mp3", "chap"):
        input_arguments[key] = Path(input_arguments[key]).resolve()
        if not input_arguments[key].exists():
            raise ValueError(f"{key} does not exist in {input_arguments[key]}")
    return input_arguments


if __name__ == '__main__':
    parser = cli_parser()
    kwargs = vars(parser.parse_args())
    kwargs = validate_input_arguments(kwargs)

    processor: ChaptersProcessor = ChaptersProcessor(mp3_file_path=kwargs["mp3"], reaper_marker_csv_path=kwargs["chap"])
    processor.convert_reaper_markers_to_mp3chap()
    processor.add_chapters_to_mp3_file()
