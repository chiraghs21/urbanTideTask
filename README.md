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

## Usage

Access the application by navigating to http://localhost:5001 in your web browser.
Use tools like Postman to upload CSV files to the API endpoint (/upload).

## Configuration

Configure the application using environment variables. Modify the docker-compose.yml file to set database credentials and other configurations as needed.

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

