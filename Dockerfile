FROM docker.io/python:latest

RUN pip3 install flask

COPY ./ /

EXPOSE 2300

ENTRYPOINT ["python3", "app.py"]
