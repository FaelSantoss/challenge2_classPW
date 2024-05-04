FROM python:latest

WORKDIR /home/pn

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

USER pn

CMD python3 main.py