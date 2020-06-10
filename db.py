import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tamboladb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE generate_no (id INTEGER, price INTEGER, cell1 INTEGER, cell2 INTEGER, cell3 INTEGER, cell4 INTEGER, cell5 INTEGER, cell6 INTEGER, cell7 INTEGER, cell8 INTEGER, cell9 INTEGER, cell10 INTEGER )")
