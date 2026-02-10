FROM python:3.11-slim
WORKDIR /app
COPY services/bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY services/bot/main.py .
CMD ["python", "main.py"]
