FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR app

COPY  requirements.txt .
COPY ./app .

RUN ls
RUN pip3 install -r ./requirements.txt

CMD ["python3", "main.py"]
EXPOSE 9000