FROM python:3.9 as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
EXPOSE 8000
COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
RUN apk add --update libpq

ENV PATH="/scripts:/py/bin:$PATH"
