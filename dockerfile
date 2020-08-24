FROM python:3.8

COPY . .

ENTRYPOINT ["python", "hello_world.py"]
