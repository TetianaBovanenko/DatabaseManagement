import mysql.connector
from dotenv import load_dotenv
import os
import random
from faker import Faker
import logging


load_dotenv()

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Retrieve database configuration
hostname = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')


def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        logging.info(f"Database '{database}' created or already exists.")
    except mysql.connector.Error as err:
        logging.error(f"Error creating database: {err}")
        raise


def create_employers_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                company_name VARCHAR(100),
                address VARCHAR(255),
                contact_number VARCHAR(50)
            )
        """)
        logging.info("Table 'employers' created or already exists.")
    except mysql.connector.Error as err:
        logging.error(f"Error creating employers table: {err}")
        raise


def create_employees_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT,
                position VARCHAR(50),
                employer_id INT,
                years_experience INT,
                salary DECIMAL(10, 2),
                FOREIGN KEY (employer_id) REFERENCES employers(id)
            )
        """)
        logging.info("Table 'employees' created or already exists.")
    except mysql.connector.Error as err:
        logging.error(f"Error creating employees table: {err}")
        raise


def generate_random_employer():
    fake = Faker()
    return {
        'company_name': fake.company(),
        'address': fake.address(),
        'contact_number': fake.phone_number()
    }


def insert_employers_data(cursor, employers):
    insert_query = """
        INSERT INTO employers (company_name, address, contact_number)
        VALUES (%s, %s, %s)
    """
    for employer in employers:
        try:
            cursor.execute(insert_query, (
                employer['company_name'],
                employer['address'],
                employer['contact_number']
            ))
            logging.info("Employer data inserted.")
        except mysql.connector.Error as err:
            logging.error(f"Error inserting employer data: {err}")
            raise


def generate_random_employee(employer_ids):
    fake = Faker()
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'age': random.randint(18, 65),
        'position': fake.job(),
        'employer_id': random.choice(employer_ids),
        'years_experience': random.randint(1, 40),
        'salary': round(random.uniform(30000, 200000), 2)
    }


def insert_employees_data(cursor, employees):
    insert_query = """
        INSERT INTO employees (first_name, last_name, age, position, employer_id, years_experience, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for emp in employees:
        try:
            cursor.execute(insert_query, (
                emp['first_name'],
                emp['last_name'],
                emp['age'],
                emp['position'],
                emp['employer_id'],
                emp['years_experience'],
                emp['salary']
            ))
            logging.info("Employee data inserted.")
        except mysql.connector.Error as err:
            logging.error(f"Error inserting employee data: {err}")
            raise


def main():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=hostname,
        port=port,
        user=username,
        password=password
    )
    cursor = conn.cursor()

    # Create the database
    create_database(cursor)

    # Close the initial connection and reconnect to the new db
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(
        host=hostname,
        port=port,
        user=username,
        password=password,
        database=database
    )
    cursor = conn.cursor()

    # Create tables
    create_employers_table(cursor)
    create_employees_table(cursor)

    # Generate random data for employers
    num_employers = 10
    employers = [generate_random_employer() for _ in range(num_employers)]
    insert_employers_data(cursor, employers)

    # Fetch employer IDs
    cursor.execute("SELECT id FROM employers")
    employer_ids = [row[0] for row in cursor.fetchall()]

    # Generate random data for employees
    num_employees = 100
    employees = [generate_random_employee(employer_ids) for _ in range(num_employees)]
    insert_employees_data(cursor, employees)

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
