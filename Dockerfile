FROM python:3.11-alpine

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080

CMD ["python", "-m", "flask", "--app", "telematon.app", "run", "--host=0.0.0.0", "--port=8080"]
