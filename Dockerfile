FROM python:3.7-slim
USER root
ADD app.py /opt/
COPY . /app
CMD ["python", "/app/app.py"]
