# uSmart Data Processing Task

## Overview

This technical task demonstrates the ability to consume data from a CSV file through a web API, perform data processing tasks including outlier detection, and insert the processed data into a SQL database. The application is containerized using Docker, making it portable and easy to deploy.

## Task Details

### Objective

The objective of this task is to:

- Develop a Python Flask application that:
  - Accepts CSV file uploads via a web API endpoint.
  - Performs basic outlier detection on the data.
  - Dynamically creates a SQL table based on the inferred schema from the CSV data.
  - Inserts the data into a PostgreSQL database container.

### Technologies Used

- **Python**: Used for backend development and data processing tasks.
- **Flask**: Micro web framework to create the API endpoints.
- **Pandas**: Library for data manipulation and analysis, used for CSV processing.
- **SQLAlchemy**: SQL toolkit and ORM used to interact with PostgreSQL database.
- **Docker**: Containerization technology for packaging the application and dependencies.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose
- Postman (Any other tool that can make http queries, this app does not have a UI)

### Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chiraghs21/urbanTideTask.git
   cd urbanTideTask/
2. **Build the docker image**

   ```bash
   docker build -t ut-app .
3. **Spin up the container**

   ```bash
   docker-compose up -d
This command starts the application in detached mode. Use -d to run containers in the background.

## Access the application:
    - Flask app: [http://localhost:5001](http://localhost:5001)
    - Adminer: [http://localhost:8080](http://localhost:8080)

## Configuration

Configure the application using environment variables. Modify the docker-compose.yml file to set database credentials and other configurations as needed.

# Approach

This project demonstrates the creation of a Flask-based web API that allows users to upload CSV files, which are then processed and inserted into a PostgreSQL database. The application also includes functionality to delete all rows from a specified table.

### 1. Flask Application Setup
The Flask application handles various routes for different functionalities:

- `/`: A simple welcome message.
- `/upload`: An endpoint to upload CSV files.
- `/delete_all_rows`: An endpoint to delete all rows from a table.

### 2. Database Configuration
- **SQLAlchemy** is used for ORM (Object Relational Mapping) to interact with the PostgreSQL database.
- The database connection parameters are stored in a constants file for easy configuration.
- The SQLAlchemy engine and session are created and managed in a dedicated module.

### 3. File Upload and Processing
The `/upload` endpoint accepts CSV files. Upon receiving a file:
- The file is read into a Pandas DataFrame.
- Outlier detection is performed using the Interquartile Range (IQR) method.
- If no outliers are detected, the table schema is inferred, and the table is created in the database.
- The data from the DataFrame is inserted into the table.

### 4. Outlier Detection
- A utility function performs outlier detection using the IQR method on the 'value' column of the DataFrame.
- Rows with values outside the acceptable range are flagged as outliers.

### 5. Table Creation and Data Insertion
- The schema for the table is inferred from the DataFrame columns.
- A new table is created in the database if it does not already exist.
- The data is inserted into the table using SQLAlchemy's `to_sql` method.

### 6. Deleting Table Rows
The `/delete_all_rows` endpoint allows deletion of all rows from a specified table:
- A utility function constructs and executes the SQL delete query within a transaction to ensure data integrity.

## Dockerization

The application and PostgreSQL database are containerized using Docker. The Docker Compose configuration sets up three services:
- **app**: The Flask application.
- **database**: The PostgreSQL database.
- **adminer**: A database management tool for interacting with the PostgreSQL database.

This setup ensures that the application can be easily deployed and run in any environment with Docker installed. The database connection in the Flask application is configured to use the Docker network to connect to the PostgreSQL service.

## Handling Potential Issues

- **Database Connectivity**: Ensuring that the application waits for the database service to be ready before attempting to connect.
- **Outlier Handling**: Proper error messages and responses are provided if outliers are detected in the uploaded data.
- **Transaction Management**: Using transactions for operations like deleting rows to maintain data integrity.

# Issues Faced and Approaches Taken

## Installing psycopg2 and Compatibility with M1 Silicon

### Issue:
- Encountered difficulties installing psycopg2, a PostgreSQL adapter for Python, on an M1 Silicon (Apple Silicon) machine.

### Approach:
- **Research**: Investigated compatibility issues of psycopg2 with M1 Silicon architecture.
- **Solution Exploration**: Explored various installation methods, including `pip` and `brew`, but faced architecture compatibility errors.
- **Binary Installation**: Found psycopg2-binary as a compatible solution with pre-built binaries for M1 Silicon.
- **Implementation**: Updated `requirements.txt` to use psycopg2-binary instead of psycopg2, ensuring compatibility.

## Database Connection Issues within Docker Containers

### Issue:
- Faced connectivity issues between Flask application (in Docker container) and PostgreSQL database (in another Docker container).

### Approach:
- **Docker Network**: Configured both containers on the same Docker network for communication.
- **Environment Variables**: Ensured accurate configuration of database connection details (host, port, user, password) via environment variables.
- **Testing and Debugging**: Used logging and Docker container logs (`docker logs <container_id>`) to diagnose connection errors.
- **Validation**: Verified connectivity with tools like `psql`, ensuring Flask application could establish connection with the database.

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

