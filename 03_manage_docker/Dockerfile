FROM python:3.7

RUN useradd -m itversity
RUN mkdir /app
RUN chown itversity:itversity /app
USER itversity

WORKDIR /app
COPY . /app
RUN python -m venv env
ENV PATH=/app/env/bin:$PATH
RUN pip install -r requirements.txt
