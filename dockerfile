FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./backend_test.db /code/backend_test.db

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]