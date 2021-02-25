FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN python3 -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8888

#CMD ["bash",  "./runApp"]

#CMD python3 manage.py runserver

CMD python3 manage.py runserver 0.0.0.0:8888
