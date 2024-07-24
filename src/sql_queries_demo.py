from sqlalchemy import create_engine, Table, MetaData, select, insert, update, delete
from sqlalchemy.orm import sessionmaker

# Replace with your actual database credentials
DATABASE_URL = "mysql+mysqlconnector://your_username:your_password@localhost/employee_db"

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(bind=engine)

# Reflect the existing tables
employers = Table('employers', metadata, autoload_with=engine)
employees = Table('employees', metadata, autoload_with=engine)

def query1():
    """Select all columns from the employees table"""
    stmt = select(employees)
    results = session.execute(stmt).fetchall()
    print("Query 1: Select all employees")
    for row in results:
        print(row)

def query2():
    """Select specific columns from the employees table"""
    stmt = select([employees.c.first_name, employees.c.salary])
    results = session.execute(stmt).fetchall()
    print("Query 2: Select employee names and salaries")
    for row in results:
        print(row)

def query3():
    """Select employees with salary greater than a specific amount"""
    stmt = select(employees).where(employees.c.salary > 60000)
    results = session.execute(stmt).fetchall()
    print("Query 3: Employees with salary > 60000")
    for row in results:
        print(row)

def query4():
    """Insert a new record into the employers table"""
    stmt = insert(employers).values(company_name='Innovate Inc', address='456 Innovation Drive', contact_number='555-6789')
    session.execute(stmt)
    session.commit()
    print("Query 4: Inserted new employer")

def query5():
    """Update a record in the employees table"""
    stmt = update(employees).where(employees.c.first_name == 'John').values(salary=90000)
    session.execute(stmt)
    session.commit()
    print("Query 5: Updated salary for employee named John")

def query6():
    """Delete a record from the employees table"""
    stmt = delete(employees).where(employees.c.first_name == 'Jane')
    session.execute(stmt)
    session.commit()
    print("Query 6: Deleted employee named Jane")

def query7():
    """Select employees with specific job positions"""
    stmt = select(employees).where(employees.c.position.in_(['Software Engineer', 'Data Scientist']))
    results = session.execute(stmt).fetchall()
    print("Query 7: Employees with specific job positions")
    for row in results:
        print(row)

def query8():
    """Count the number of employees"""
    stmt = select([employees.c.id.count()])
    result = session.execute(stmt).scalar()
    print(f"Query 8: Total number of employees: {result}")

def query9():
    """Select employees and order by salary descending"""
    stmt = select(employees).order_by(employees.c.salary.desc())
    results = session.execute(stmt).fetchall()
    print("Query 9: Employees ordered by salary descending")
    for row in results:
        print(row)

def query10():
    """Select employees with a limit and offset"""
    stmt = select(employees).limit(5).offset(10)
    results = session.execute(stmt).fetchall()
    print("Query 10: Employees with limit and offset")
    for row in results:
        print(row)

def main():
    query1()
    query2()
    query3()
    query4()
    query5()
    query6()
    query7()
    query8()
    query9()
    query10()

if __name__ == "__main__":
    main()
