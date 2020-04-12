import openpyxl
import sqlite3
from sqlite3 import Error

path = '../data/'
majors = ['Biological Sciences', 'Business', 'Communication Arts',
            'Computer Information Systems (1)', 'Computer Science (1)',
            'EET w_ CT Option (1)', 'Electrical Engineering Technology (1)',
            'English (1)', 'English Teaching (1)', 'History (1)',
            'Mechanical Engineering Technology (1)', 'Politics and Society (1)',
            'Psychology (1)', 'Sign Language Interpretation (1)'
        ]
ext = '.xlsx'
db_file = '../../db.sqlite3'

def fixMajorList(majors):
    fixedMajors = []
    stripMe = '(1)'

    for item in majors:
        fixedItem = item.strip(stripMe)
        fixedItem = fixedItem.strip()
        fixedMajors.append(fixedItem)
    return(fixedMajors)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_school(conn, major):
    sql = ''' INSERT INTO transfer_major(major_name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [major])
    return cur.lastrowid

if __name__ == '__main__':
    major_list = fixMajorList(majors)
    conn = create_connection(db_file)
    with conn:
        for major in major_list:
            task = create_school(conn, major)
