# Employee Database Management

! [Database Management Logo](https://github.com/TetianaBovanenko/DatabaseManagement/blob/main/PYTHON%20PROJECT.png?raw=true)

## Project Description

This project is a Python script that interacts with a MySQL database to manage employee records. The script performs the following tasks:

1. **Database and Table Creation**: Creates a MySQL database named `employee_db` and two tables within it:
   - `employers`: Contains information about companies, including company name, address, and contact number.
   - `employees`: Stores employee details, including names, age, position, years of experience, salary, and a foreign key linking to the `employers` table.

2. **Data Generation**: Uses the `Faker` library to generate realistic, random data for both employers and employees. This includes generating fake names, job titles, company names, addresses, and contact information.

3. **Data Insertion**: Inserts the generated random data into the `employers` and `employees` tables.

## Features

- **Database Creation**: Automatically creates a database if it does not exist.
- **Table Creation**: Creates tables with appropriate schema and relationships.
- **Random Data Generation**: Generates realistic random data for testing or development purposes.
- **Data Insertion**: Inserts the generated data into the database tables.

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python Libraries:
  - `mysql-connector-python`
  - `Faker`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/employee_db_project.git
   cd employee_db_project
