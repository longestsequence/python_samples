FROM python:3.9
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY consumer.py .

CMD ["python", "/app/consumer.py"]