FROM python:3.10
WORKDIR /jin
COPY requirements.txt /jin/
RUN pip install -r requirements.txt
COPY . /jin
CMD python jin.py