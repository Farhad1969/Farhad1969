FROM python:3.10-slim
RUN apt-get update && apt-get install -y netcat-openbsd
WORKDIR /app
COPY server.py .
CMD ["python", "server.py"]