From python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install -r requirement.txt
Expose 5000
ENTRYPOINT ["python"]
cmd ["print_req.py"]
