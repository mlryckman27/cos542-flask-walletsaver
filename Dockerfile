FROM python:3.10-alpine
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./requirements.txt /app/requirements.txt
RUN mkdir /app/templates
COPY . /app
RUN pip install -r requirements.txt
CMD ["flask", "run"]