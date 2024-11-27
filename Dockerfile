FROM python:3.12

WORKDIR /app 

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./app app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
