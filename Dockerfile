FROM python:3.6-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
        postgresql-client && rm -rf /var/lib/apt/lists/*

RUN adduser -D stic

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
COPY . .

## COPY app app

RUN chmod +x boot.sh

RUN chown -R stic:stic ./
USER stic

EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


