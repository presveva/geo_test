FROM python:3.7.2-slim
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
ADD . /opt/app/
WORKDIR /opt/app
CMD gunicorn --bind 0.0.0.0:$PORT -t 90 -w 4 app:app --log-level=DEBUG
