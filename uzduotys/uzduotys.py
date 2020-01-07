import sqlite3


def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    connection.close()


def querry_database(query, parameters=None):
    try:
        connection, cursor = open_connection()
        if parameters:
            cursor.execute(query)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)
    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()


def get_first():
    query = """SELECT first_name, last_name, salary FROM employees 
               WHERE salary < 10000 OR salary > 15000  """
    querry_database(query)

def get_second():
    query = """SELECT first_name, last_name, department_id FROM employees
                WHERE department_id = 30 OR department_id = 100
                ORDER BY department_id ASC """
    querry_database(query)

def get_third():
    query = """SELECT first_name, last_name, salary, department_id FROM employees 
               WHERE (salary < 10000 OR salary > 15000) AND (department_id = 30 OR department_id = 100)"""

    querry_database(query)


def get_fourth():
    query = """SELECT first_name, job_title FROM employees 
               WHERE (first_name LIKE "%b%") AND (first_name LIKE "%c%") """

    querry_database(query)


def get_fifth():
    query = """SELECT last_name, salary, job_id FROM employees 
               WHERE (job_id = 'IT_PROG' OR job_id = 'SH_CLERK') AND (NOT salary = 4500 OR 10000 OR 15000) """

    querry_database(query)


def get_sixth():
    query = """SELECT last_name FROM employees 
               WHERE LENGTH(last_name) = 6 """

    querry_database(query)


def get_seventh():
    query = """SELECT last_name FROM employees 
               WHERE last_name LIKE '__e%' """

    querry_database(query)




# get_first()
# get_second()
# get_third()
# get_fourth()
# get_fifth()
# get_sixth()
get_seventh()
