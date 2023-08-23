FROM python:3.11.4

WORKDIR /app

COPY . .

RUN pip install poetry && poetry install

CMD ["flask", "--app","main", "run"]