FROM python:3.8

COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "hello_world.py"]
