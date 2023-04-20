FROM python:3.10-alpine
WORKDIR /app
ENV FLASK_APP app.py
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]