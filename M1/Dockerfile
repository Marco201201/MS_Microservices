FROM python:3.11
WORKDIR /M1
COPY ./requirements.txt /M1/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /M1/requirements.txt
COPY ./app /M1/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]