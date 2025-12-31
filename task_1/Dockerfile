FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY main.py .

# Expose the port the app runs on
EXPOSE 10000

# Command to run the application
CMD ["python", "main.py", "--opt", "runserver"]