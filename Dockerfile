 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /tshirtshop
 WORKDIR /tshirtshop
 ADD requirements.txt /tshirtshop
 RUN pip install -r requirements.txt
 EXPOSE 8000

 ADD . /tshirtshop/
