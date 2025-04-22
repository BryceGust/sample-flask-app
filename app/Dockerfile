FROM python:3.12-alpine

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir flask

EXPOSE 80

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]

