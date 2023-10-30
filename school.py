# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/school.sqlite')
dbb = conn.cursor()

def students_from_city(db, city):
    """return a list of students from a specific city"""
    query = f'''
    SELECT * FROM students
    WHERE birth_city = "{city}"
    '''
    db.execute(query)
    results = db.fetchall()
    return results
# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py

#print(students_from_city(db, 'London'))
