FROM python:3.7

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP app.py
ENV FLASK_ENV development

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
