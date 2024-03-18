# COMP3005-A3-Q1
Application that allows for CRUD (Create, Read, Update, Delete) operations to be done on a PostgreSQL database called 'students'.

Setup Instructions:

This application implements a function that connects to a PostgreSQL database. This function requires certain credentials/information in order to connect to and access the database. 

The application looks in a '.env' file, which contains the host, port, username, password, and database name with the variable names 'db_host', 'db_port', 'db_user', 'db_password', and 'db_name' respectively.

Therefore, when running this application, the user must create a '.env' file with the proper credentials filled into the above variable names in order to correctly connect to their database.

Once the above is complete, the user can run the python file 'db_connection.py' using the 'python db_connection.py' command. If the credentials in the '.env' file are correct, the interface for the application will be visible and usable.

YouTube demonstration link: https://www.youtube.com/watch?v=CZTsEh7k8h4&ab_channel=JacobSevigny