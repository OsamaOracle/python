import cx_Oracle
try:
 conn = cx_Oracle.connect("hr", "oracle", "dbhostname/orcl")
 sql="""SELECT d.* FROM departments d, locations l WHERE
       l.city = :city AND d.location_id = l.location_id"""
 column_length=[5, 22, 6, 5]
 cursor = conn.cursor()
 for row in cursor.execute(sql, city = 'Seattle'):
   for i in range (len(row)):
     print(str(row[i]).ljust(column_length[i]), end='')
   print()
except cx_Oracle.DatabaseError as exc:
  err, = exc.args
  print("Oracle-Error-Code:", err.code)
  print("Oracle-Error-Message:", err.message)
finally:
  cursor.close()
  conn.close()

