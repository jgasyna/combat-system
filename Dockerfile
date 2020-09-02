FROM python:3.7.4-alpine3.10

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

CMD [ "python", "-u", "game_play.py" ]