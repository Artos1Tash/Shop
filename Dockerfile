FROM python:3.10-alpine
WORKDIR /Shop/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY req.txt /Shop/
RUN pip install -r req.txt
COPY . /Shop/

