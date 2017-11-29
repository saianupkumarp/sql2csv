#-------------------------------------- Chnage Log -------------------------------------------
__author__ = "Anup Kumar"
__copyright__ = "Copyright 2017"
__credits__ = ["Anup Kumar"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Anup Kumar"
__status__ = "Production"
#------------------------------------ Change Details ------------------------------------------
# 11/29/2017 - Anup Kumar - Initial code to export all tables data to csv from sql server
#----------------------------------------------------------------------------------------------
import os, csv, pymssql

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
FILE_NAME_PATTERN = 'tbl_'

#SQL Server Config
SERVER = 'Server Name'
USERNAME = 'SQL Auth Username'
PASSWORD = 'SQL Auth password'
DATABASE = 'Database Name'

def sql2csv(DIR_PATH, FILE_NAME_PATTERN):
    conn = pymssql.connect(SERVER, USERNAME, PASSWORD, DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES')
    tbls = cursor.fetchall()
    for row in tbls:
        print row[0] + '.' + row[1]
        with open(os.path.join(DIR_PATH, '_Output', 'SQLOutput', FILE_NAME_PATTERN + row[0] + '.' + row[1] + '.csv'), 'wb') as tbl_output:
            cursor.execute('SELECT * FROM ' + row[0] + '.' + row[1])
            writer = csv.writer(tbl_output)
            writer.writerow([ i[0] for i in cursor.description ]) # heading
            writer.writerows(cursor.fetchall())

if __name__ == '__main__':
    sql2csv(DIR_PATH, FILE_NAME_PATTERN)