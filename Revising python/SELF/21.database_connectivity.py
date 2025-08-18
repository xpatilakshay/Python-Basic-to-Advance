# import mysql.connector

# con = mysql.connector.connect(
#  host="Localhost",
#  user="root",
#  password="Root@123",
#  database="company_db"
# )

# cursor = con.cursor()

# cursor.execute('Select * from employee')

# for row in cursor.fetchall():
#     print(row)


# con.close()



import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "Root@123",
    database = "company_db"
)

cursor = conn.cursor()

cursor.execute("Select * from employee")

for data in cursor.fetchall():
    print(data)

conn.close()