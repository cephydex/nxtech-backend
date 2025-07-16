FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY .env .env

EXPOSE 80

# Define the command to run your FastAPI app with Uvicorn
ENTRYPOINT [ "uvicorn", "main:app" ]
CMD ["--host", "0.0.0.0", "--port", "80", "--reload"]
