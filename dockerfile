FROM python:3.10.4
COPY requirements.txt /tmp/requirements.txt
COPY ./app app/
RUN python3 -m pip install -r /tmp/requirements.txt
WORKDIR /app
RUN ln -fs /usr/share/zoneinfo/America/Belem /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
CMD ["python3", "main.py"]