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
# get_seventh()


def get_second_first():
    query = """SELECT DISTINCT job_id FROM employees """

    querry_database(query)


def get_second_second():
    query = """SELECT SUM(salary) as total_salary FROM employees"""

    querry_database(query)


def get_second_third():
    query = """SELECT salary FROM employees
            ORDER by salary ASC
            LIMIT 1"""

    querry_database(query)


def get_second_fourth():
    query = """SELECT salary FROM employees
            ORDER by salary DESC
            LIMIT 1"""

    querry_database(query)


def get_second_fifth():
    query = """SELECT AVG(salary) as avg_salary, COUNT(employee_id) FROM employees
            WHERE department_id = 90"""

    querry_database(query)


def get_second_sixth():
    query = """SELECT MIN(salary), MAX(salary), SUM(salary), AVG(salary) FROM employees"""

    querry_database(query)


def get_second_seventh():
    query = """SELECT job_id, COUNT(*)  FROM employees
               GROUP BY job_id"""

    querry_database(query)


def get_second_eigth():
    query = """SELECT (MAX(salary) - MIN(salary)) as DIF_salary FROM employees"""

    querry_database(query)


def get_second_ninth():
    query = """SELECT department_id, SUM(salary) FROM employees
               GROUP BY department_id"""

    querry_database(query)


def get_second_tenth():
    query = """SELECT AVG(salary), job_id FROM employees
                WHERE NOT job_id = 'IT_PROG'
               GROUP BY job_id"""

    querry_database(query)


def get_second_eleventh():
    query = """SELECT MIN(salary), manager_id, job_id FROM employees
                GROUP by manager_id
               """

    querry_database(query)



# get_second_first()
# get_second_second()
# get_second_third()
# get_second_fourth()
# get_second_fifth()
# get_second_sixth()
# get_second_seventh()
# get_second_eigth()
# get_second_ninth()
# get_second_tenth()
# get_second_eleventh()


def create_view():
    query = """CREATE VIEW IF NOT EXISTS names
            as
            SELECT
                first_name,
                last_name
            FROM employees"""
    querry_database(query)
    querry_database("SELECT * FROM names")


# create_view()

def get_all():
    query = "SELECT * FROM employees"
    querry_database(query)


def get_3_1():
    query = """SELECT first_name, last_name, salary  FROM employees
    WHERE salary > (SELECT salary FROM employees WHERE last_name="Bull")"""
    querry_database(query)


def get_3_2():
    query = """SELECT first_name, last_name, job_id, manager_id  FROM employees
    WHERE employee_id IN (SELECT manager_id FROM employees)"""
    querry_database(query)


def get_3_3():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)"""
    querry_database(query)


def get_3_4():
    query = """SELECT first_name, last_name, salary, job_id FROM employees
        WHERE salary = (SELECT min_Salary FROM jobs WHERE employees.job_id=jobs.job_id)"""
    querry_database(query)


def show_ids():
    query = """SELECT Department_ID FROM departments"""
    querry_database(query)


def get_3_5():
    query = """SELECT first_name, last_name, salary, job_id FROM employees
        WHERE department_id IN (SELECT department_id FROM department_name LIKE 'IT%' AND 
        (salary > SELECT AVG(salary) from employees)"""
    querry_database(query)


def get_3_6():
    query = """SELECT first_name, salary, job_id FROM employees
            ORDER BY salary DESC
            LIMIT 3"""
    querry_database(query)


def get_3_7():
    query = """SELECT first_name, last_name FROM employees
                WHERE manager_id IN (SELECT employee_id FROM employees
                WHERE department_id IN (SELECT department_id FROM departments
                WHERE location_id IN (SELECT location_id FROM locations WHERE country_id= 'US')))"""
    querry_database(query)


# get_3_2()
# get_all()
# get_3_1()
# get_3_3()
# get_3_4()
get_3_5()
# get_3_6()
# get_3_7()
# show_ids()