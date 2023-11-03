##This file is written by Yutong Yang. 
# It is used to  transfer the data from .db to .csv, make the data easy to read and deal with
# After running the data, we can access 3 .csv data document,
# which I named as practice_level_prescribing.csv、practices.csv、sqlite_sequence.csv
#  
import sqlite3
import csv
import filecmp 
import sqlite3

def sql2csv (fileIn, fileOut,sql) :
	conn = sqlite3.connect(fileIn)
	cursor = conn.cursor()
	#sql = """select name from sqlite_master where type='table' order by name"""
	#sql = """select * from sqlite_sequence"""
	cursor.execute(sql)
	results = cursor.fetchall()
    #print(results)
    #print(type(results))
	with open(fileOut,'w',newline='') as fp:
	    writer=csv.writer(fp)
	    writer.writerows(results)
	conn.close()

sql2csv("abxdb.db", "practice_level_prescribing.csv",sql = """select * from practice_level_prescribing""")
sql2csv("abxdb.db", "practices.csv",sql = """select * from practices""")
sql2csv("abxdb.db", "sqlite_sequence.csv",sql = """select * from sqlite_sequence""")
