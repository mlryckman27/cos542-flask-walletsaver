FROM python:3.10-alpine
WORKDIR /app
ENV FLASK_APP app.py
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
#CMD ["cd", "app"]
CMD ["flask", "run"]