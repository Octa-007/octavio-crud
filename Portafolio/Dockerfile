FROM python:3

RUN mkdir -p /opt/services/flaskapp/src
RUN mkdir -p /opt/services/flaskapp/src/data
COPY requeriments.txt /opt/services/flaskapp/src
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requeriments.txt
COPY . /opt/services/flaskapp/src
EXPOSE 7979
CMD ["python", "server.py"]