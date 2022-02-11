import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
my_cursor = conn.cursor()
conn = pyodbc.connect(
                        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
my_cursor = conn.cursor()
sql = "SELECT FROM student WHERE ID_STUDENT=?"
val = (self.var_id.get(),)
my_cursor.execute(sql, val)
conn.commit()
conn.close()
print(a[0][0])
conn.commit()
conn.close()