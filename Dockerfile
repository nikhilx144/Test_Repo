FROM python:3.12

WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 8090

CMD ["python", "app.py"]