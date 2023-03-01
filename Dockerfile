FROM python:3.11.1-slim-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /src

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY . /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
