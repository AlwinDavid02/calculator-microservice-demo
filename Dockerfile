FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY home-page.py ./
COPY templates/ ./templates/

EXPOSE 5000 

CMD [ "python", "add.py" ]