FROM python:3.8
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app
WORKDIR /app
COPY ./app  /app
EXPOSE 8000
ENTRYPOINT ["uvicorn"]
CMD ["mlfastapi:app","--host","0.0.0.0"]

