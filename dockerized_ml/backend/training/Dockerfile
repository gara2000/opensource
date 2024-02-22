FROM python:3

WORKDIR /usr/src/app

RUN pip install fastapi uvicorn
RUN pip install python-multipart

COPY . .

RUN chmod +x entry_point.sh

ENTRYPOINT [ "./entry_point.sh" ]