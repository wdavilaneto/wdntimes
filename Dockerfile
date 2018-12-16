#FROM python:3.6-alpine
FROM python:3.7.1
RUN apk update && apk add postgresql-dev g++ python3-dev musl-dev postgresql-client
#RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client &&
RUN rm -rf /var/lib/apt/lists/*

RUN adduser -D stic

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install --upgrade setuptools
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
COPY . .

RUN chmod +x boot.sh

RUN chown -R stic:stic ./
USER stic

EXPOSE 8000
CMD ["/boot.sh"]

#ENTRYPOINT ["./boot.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
