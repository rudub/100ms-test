From python:3.8
WORKDIR /app
COPY app.py /app 
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
cmd ["app.py"]
