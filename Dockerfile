FROM python:3.12-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD . .

EXPOSE 8000 
CMD ["waitress-serve", "--port=8000", "index:app"]