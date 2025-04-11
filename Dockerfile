FROM python:3.13.2-slim

WORKDIR WheelsAPI/

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "app/main.py" ]
