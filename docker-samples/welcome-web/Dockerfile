FROM python:3

#Set the working dir
WORKDIR /usr/src/app

#Copy the code here
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

CMD ["python", "./app.py"]
