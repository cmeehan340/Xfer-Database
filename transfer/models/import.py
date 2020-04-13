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

def fixMajorList(majors):
    fixedMajors = []
    stripMe = '(1)'

    for item in majors:
        fixedItem = item.strip(stripMe)
        fixedItem = fixedItem.strip()
        if (fixedItem == ("EET w_ CT Option")):
            fixedItem = "EET with CT Option"
        fixedMajors.append(fixedItem)
    return fixedMajors

def create_major(conn, major):
    sql = ''' INSERT INTO transfer_major(major_name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [major])
    return cur.lastrowid

def create_school(conn, school, majorid):
    sql = ''' INSERT INTO transfer_school(school_name, major_id_id) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, [school, majorid])
    return cur.lastrowid

if __name__ == '__main__':
    conn = create_connection(db_file)
    major_list = fixMajorList(majors)

    with conn:
        for major in major_list:
            task = create_major(conn, major)
        idx = 0
        for major in majors:
            school_list = create_school_list(major)
            with conn:
                for school in school_list:
                    task = create_school(conn, school, major_list[idx])
            idx+=1
