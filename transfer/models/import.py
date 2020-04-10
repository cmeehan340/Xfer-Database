import openpyxl
import sqlite3
from sqlite3 import Error



def getSchools(sheet):
    school_list = []
    for row_idx in range(sheet.min_row+1, sheet.max_row + 1):
        cell_content = sheet.cell(row=row_idx, column=1).value
        if cell_content not in school_list:
            if cell_content != None:
                if cell_content not in ['NHTI', 'Colby Sawyer', 'UNH Durham']:
                    school_list.append(cell_content)
    return school_list


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_school(conn, school):
    sql = ''' INSERT INTO transfer_school(school_name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [school])
    return cur.lastrowid

if __name__ == '__main__':
    file = '../data/Business.xlsx'
    db_file = '../../db.sqlite3'
    wb = openpyxl.load_workbook(file)

    sheet = wb.active
    school_list = getSchools(sheet)
    print(school_list)
    conn = create_connection(db_file)
    with conn:
        for school in school_list:
            task = create_school(conn, school)
