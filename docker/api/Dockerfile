FROM amazon/aws-lambda-python:3.9

RUN pip install --upgrade pip
RUN pip install poetry
RUN pip install flask  # Thêm dòng này để cài đặt Flask
RUN poetry install

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN flask --app main run