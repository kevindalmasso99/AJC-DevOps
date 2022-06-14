FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3.10 
    
RUN apt-get install -y python3-pip

WORKDIR /kdalmasso

COPY . .

CMD ["python3", "main.py"]

