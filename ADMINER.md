# Using Adminer to Manage Your PostgreSQL Database

Adminer is a web-based database management tool that allows you to interact with your databases through a user-friendly interface. Here's a simple guide on how to use Adminer to manage your PostgreSQL database:

## Accessing Adminer

1. **Start Your Docker Containers:**
   Ensure your Docker containers are running. You can start your containers using Docker Compose with the appropriate command.

2. **Open Adminer in Your Browser:**
   Open your web browser and navigate to: http://localhost:8080


## Logging into Adminer

1. **Database Type:**
Select `PostgreSQL` from the `System` dropdown menu.

2. **Server:**
Enter `database` (this is the service name defined in your `docker-compose.yml`). If you're connecting to a local PostgreSQL instance, use `localhost`.

3. **Username:**
Enter the PostgreSQL username. For the provided setup, the default username is `docker`.

4. **Password:**
Enter the PostgreSQL password. For the provided setup, the default password is `docker`.

5. **Database:**
Enter the database name you want to manage. For the provided setup, the default database name is `exampledb`.

6. **Click `Login`:**
After filling in the required fields, click the `Login` button to access the Adminer interface.

## Using Adminer

Once logged in, you can perform various database management tasks, such as:

- Viewing tables
- Executing SQL queries
- Importing and exporting data
- Editing data

Adminer provides a comprehensive set of features to manage your database efficiently, making it an excellent tool for database administration.

For more detailed instructions on using Adminer, refer to the [Adminer documentation](https://www.adminer.org/docs/).

Now you are ready to manage your PostgreSQL database with ease using Adminer!
