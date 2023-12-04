"""
Using the speaker diarization from here:
https://replicate.com/meronym/speaker-diarization
"""
import argparse
import json
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)


class DiarizationParser:
    @classmethod
    def parse(cls, diarization_json_path: str):
        """
        data = {
            "segments": [
                {
                    "speaker": "A",
                    "start": "0:00:15.094688",
                    "stop": "0:00:33.066563",
                },
                {
                    "speaker": "B",
                    "start": "0:00:33.066563",
                    "stop": "0:00:51.527813",
                },
                ....
            }
        """
        data = json.load(open(diarization_json_path))
        df = pd.DataFrame(data["segments"])
        # Convert time format to HH:MM:SS
        df["start"] = pd.to_datetime(df["start"]).dt.strftime("%H:%M:%S")
        df["stop"] = pd.to_datetime(df["stop"]).dt.strftime("%H:%M:%S")
        # Add a 'Name' column with "marker" prefix and row number
        df["Name"] = "marker" + (df.index + 1).astype(str)
        # Rename columns
        df = df.rename(columns={"speaker": "#", "start": "Start", "stop": "End"})
        # Create a 'Length' column and leave it empty
        df["Length"] = ""
        # Reorder columns
        df = df[["#", "Name", "Start", "End", "Length"]]
        logging.info(f"Writing output to output.csv")
        df.to_csv("output.csv", index=False)
        # print(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to diarization json file", required=True)
    args = parser.parse_args()
    p_diarization_json_path = args.file
    DiarizationParser.parse(p_diarization_json_path)
