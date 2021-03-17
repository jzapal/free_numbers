FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["check_free_numbers.py"]
ENTRYPOINT ["python3"]