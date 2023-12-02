FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV CALENDAR_ID=id
ENV GOOGLE_API=api
ENV GOOGLE_CREDENTIALS_JSON=path/to/file
ENV GOOGLE_CREDENTIALS_PICKLE=path/to/file

CMD ["python", "main.py"]