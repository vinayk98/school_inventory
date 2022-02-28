#definde constant
import mysql.connector
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
mysql_databse = "db_school"


def get_db_cursor():
# create connection and return db cursor
    connection = mysql.connector.connect(
        host=MYSQL_HOST,user=MYSQL_USER,database=mysql_databse,password=MYSQL_PASSWORD

    )
    return connection
