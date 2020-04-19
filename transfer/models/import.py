import openpyxl
import sqlite3
from sqlite3 import Error

path = '../data/'
majors = ['Biological Sciences', 'Business', 'Communication Arts',
            'Computer Information Systems', 'Computer Science',
            'EET with CT Option', 'Electrical Engineering Technology',
            'English', 'English Teaching', 'History',
            'Mechanical Engineering Technology', 'Politics and Society',
            'Psychology', 'Sign Language Interpretation'
        ]
ext = '.xlsx'
db_file = '../../db.sqlite3'



def addSheetToList(sheet, school_list):
    for row_idx in range(sheet.min_row+1, sheet.max_row + 1):
        cell_content = sheet.cell(row=row_idx, column=1).value
        if cell_content not in school_list:
            if cell_content != None:
                    school_list.append(cell_content)
    return school_list


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_school_list(major):
    school_list = []
    file = path + major + ext
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    school_list = addSheetToList(sheet, school_list)
    return school_list



def create_major(conn, major):
    sql = ''' INSERT INTO transfer_major(major_name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [major])
    return cur.lastrowid

def create_school(conn, school):
    sql = ''' INSERT INTO transfer_school(school_name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [school])
    return cur.lastrowid

if __name__ == '__main__':
    conn = create_connection(db_file)
    with conn:
        for major in majors:
            task = create_major(conn, major)
        school_list = create_school_list(majors)
        for school in school_list:
            school_task = create_school(conn, school)
