import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lifechoices",
  password="@Lifechoices1234",
  database="lifechoicesonline"
)
#
# adding users into the system
# *******************************************************************************

# mycursor = mydb.cursor()

# sql = "INSERT INTO users (full_name, username, password ) VALUES (%s, %s, %s)"
# val = [
#     ('Shane kolkoto', 'ShaneK', '2345')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

# Inserting into the admin
# **********************************************************************************
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO admin (full_name, username, password ) VALUES (%s, %s, %s)"
# val = [
#     ('Shane jhhjlkjlk', 'ShaneJ', '2345')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

# Inserting into the visitors
# **********************************************************************************
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO visitors (full_name, username, password ) VALUES (%s, %s, %s)"
# val = [
#     ('Shane jhhjlkjlk', 'ShaneJ', '2345')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

# Select fields from the users table
# ********************************************************************************************
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="lifechoices",
#   password="@Lifechoices1234",
#   database="lifechoicesonline"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM users")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# Select fields from the admin table
# ********************************************************************************************
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="lifechoices",
#   password="@Lifechoices1234",
#   database="lifechoicesonline"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM admin")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# Select fields from the visitors table
# ********************************************************************************************
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="lifechoices",
#   password="@Lifechoices1234",
#   database="lifechoicesonline"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM visitors")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
