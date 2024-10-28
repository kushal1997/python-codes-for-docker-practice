FROM python:3.11-slim

WORKDIR /myapp

COPY ./myapp.py .

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python" , "myapp.py" ]