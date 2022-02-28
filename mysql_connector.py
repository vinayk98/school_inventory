import mysql.connector
connection=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="db_school")
connection.cursor()
cursor=connection.cursor()
cursor.execute("DESC teacher;")
for i in cursor.fetchall():
    print(i)