FROM python:3.8

RUN pip3 install mp3chaps
COPY processReaperMarkers.py /opt/

CMD ["python3", "/opt/processReaperMarkers.py", "--mp3", "/opt/data/snd.mp3", "--chap", "/opt/data/chap.csv"]
