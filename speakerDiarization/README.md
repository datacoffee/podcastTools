# Speaker diarization JSON to CSV transformer
This script transforms the JSON output of the speaker diarization script into a CSV file.

Pipeline:
- record your multi-host podcast
- run the speaker diarization model (for example, https://replicate.com/meronym/speaker-diarization)
- run this script to transform the JSON output into a CSV file
- import CSV into REAPER's "Region/Marker Manager" to create regions for each speaker
- jump faster through markers to check if the topic has changed