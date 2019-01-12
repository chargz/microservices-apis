FROM python3.7

RUN pip install flask

RUN mkdir /root/hasher
WORKDIR /root/hasher

COPY ./ ./

EXPOSE 5000

CMD["python", "hasher.py"]