FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN chmod +x cal.py
CMD ["python", "cal.py"]
