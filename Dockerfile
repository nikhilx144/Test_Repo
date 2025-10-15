FROM python:3.12

WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 5100

CMD ["python", "app.py"]