FROM python:3.8

COPY . .

ENTRYPOINT ["python", "test.py"]
