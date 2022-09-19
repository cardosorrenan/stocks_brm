FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /usr/src/app