FROM python:3.9
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY producer.py .

CMD ["python", "/app/producer.py"]