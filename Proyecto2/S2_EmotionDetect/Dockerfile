FROM python:3.8

ADD emotionDetect.py .

ADD FacesDataBase /usr/local
ADD DataBase /usr/local

RUN pip install opencv-python-headless
RUN pip install deepface

CMD [ "python", "./emotionDetect.py"]