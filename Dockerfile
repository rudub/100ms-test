From python:3.8
WORKDIR /app
COPY . /app 
RUN pip3 install -r requirement.txt
EXPOSE 5000
cmd ["python3", "app.py"]
