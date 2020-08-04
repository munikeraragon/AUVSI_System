FROM python:3.8


RUN apt install python3-pip
RUN python3 -m pip3 install Django
RUN pip3 install jsonify
RUN pip3 install django-jsonify

