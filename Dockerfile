FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./grow-lot-habits /code/grow-lot-habits

EXPOSE 8000

CMD ["python", "grow-lot-habits/manage.py", "runserver", "0.0.0.0:8000"]