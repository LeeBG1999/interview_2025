# FastAPI CSV Uploader

## Methodology

This project is designed to provide a simple API for uploading CSV files using FastAPI. The application allows users to send CSV data via a POST request, which is then processed and validated. The architecture is modular, separating the API routes, services, and main application logic to enhance maintainability and scalability.

The application is containerized using Docker, allowing for easy deployment and consistent environments across different systems. Docker Compose is used to manage the application and its dependencies, ensuring that the FastAPI service runs smoothly.

## How to Run


1. **Build and Run the Application**  
   Use Docker Compose to build and run the application:  
   ```
   docker-compose up --build
   ```

2. **Access the Application**  
   Once the application is running, you can access it at `http://localhost:10000`. You can use tools like Postman or curl to send POST requests with CSV files to the `/upload` endpoint.

3. **Stop the Application**  
   To stop the application, press `CTRL+C` in the terminal where Docker Compose is running, or run:  
   ```
   docker-compose down
   ```

Make sure you have Docker and Docker Compose installed on your machine before running the application.