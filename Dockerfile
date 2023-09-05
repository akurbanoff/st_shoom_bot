FROM python:3.11.0rc1

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /st_shoom_bot

WORKDIR /st_shoom_bot

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x /st_shoom_bot/docker/app.sh

CMD ["/st_shoom_bot/docker/app.sh"]