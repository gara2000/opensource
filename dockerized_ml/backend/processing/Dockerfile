FROM python:3

WORKDIR /usr/src/app

RUN pip install fastapi uvicorn
RUN pip install python-multipart
RUN pip install pandas
RUN pip install pymongo

COPY . .

RUN chmod +x entry_point.sh

ENTRYPOINT [ "./entry_point.sh" ]