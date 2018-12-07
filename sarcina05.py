import mysql.connector


#   Afiseaza continutul cursorului
def print_cursor(cursor):
    for element in cursor:
        print(element)


#   Conectarea la baza de date
mydb = mysql.connector.connect(
  host="localhost",
  user="phpmyadmin",
  passwd="26264605050"
)
#   Definirea cursorului
mycursor = mydb.cursor(buffered=True)

#   Crearea, in caz ca nu exista, a tabelului capitalele
mycursor.execute("CREATE DATABASE IF not exists sarcina5")
mycursor.execute("use sarcina5")

mycursor.execute("CREATE TABLE if not exists Numbers(Val INTEGER)")
mycursor.execute("truncate table Numbers")
mycursor.execute("INSERT INTO Numbers Values(1)")
mycursor.execute("INSERT INTO Numbers Values(1)")
mydb.commit()
mycursor.execute("SELECT * FROM Numbers WHERE 1/0")
print_cursor(mycursor)
mycursor.execute("SELECT * FROM Numbers WHERE 1/0 AND Val > 0")
print_cursor(mycursor)
mycursor.execute("SELECT * FROM Numbers WHERE Val > 0 AND 1/0")
print_cursor(mycursor)
