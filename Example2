#This example from live demo presentation - Using Python with Oracle - OUGF 
import cx_Oracle
conn = cx_Oracle.connect("hr", "hr", "192.168.174.132/orcl")
sql = "SELECT * FROM departments"
cursor = conn.cursor()
cursor.execute(sql)
for each in cursor.description:
  print(each[0:2])
