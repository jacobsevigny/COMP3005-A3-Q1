import psycopg2
from psycopg2 import Error, OperationalError
from dotenv import dotenv_values

# Connects to PostgreSQL DB with the credentials from .env file
def PostgreSQLConnection():
    try:
        db_vars = dotenv_values('.env')
        
        db_host = db_vars.get('db_host')
        db_port = db_vars.get('db_port')
        db_user = db_vars.get('db_user')
        db_password = db_vars.get('db_password')
        db_name = db_vars.get('db_name')

        connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
        return connection
    
    except OperationalError as e:
        print(f"Error has occurred trying to connect to the database: {e}")
        return None

# Gets all students from the DB
def getAllStudents():
    try:
        conn = PostgreSQLConnection()

        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")

            print('\nList of Students:\n')

            rows = cursor.fetchall()
            for row in rows:
                print('Student ID:', row[0])
                print('First Name:', row[1])
                print('Last Name:', row[2])
                print('Email:', row[3])
                print('Enrollment Date:', row[4])
                print('\n')

            cursor.close()
            conn.close()

    except Error as e:
        print(f"Error has occurred trying to fetch student info from the database: {e}")

# Adds a student to the DB
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        conn = PostgreSQLConnection()

        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
            conn.commit()

            print("\nStudent added.")

            cursor.close()
            conn.close()

    except Error as e:
        print(f"Error has occurred trying to add student to the database: {e}")

# Updates the email of a student
def updateStudentEmail(student_id, new_email):
    try:
        conn = PostgreSQLConnection()

        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
            conn.commit()

            print("\nEmail updated successfully")

            cursor.close()
            conn.close()

    except Error as e:
        print(f"Error has occurred trying to update student's email in the database: {e}")

# Deletes a student from the DB
def deleteStudent(student_id):
    try:
        conn = PostgreSQLConnection()

        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            conn.commit()

            print("Student deleted successfully")
            
            cursor.close()
            conn.close()

    except Error as e:
        print(f"Error has occurred trying to delete student from the database: {e}")

#Creates interface for selecting operations to be done on database
def main():
    while True:
        print("\n\n1. Get all students")
        print("2. Add Student")
        print("3. Update Student Email")
        print("4. Delete Student")
        print("5. Terminate App\n\n")
        
        choice = input("Please enter # corresponding to desired function: ")
        
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("\nEnter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (yyyy-mm-dd): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            deleteStudent(student_id)
        else:
            break

main()
