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
mycursor = mydb.cursor()

#   Crearea bazei de date in caz ca nu exista, a tabelului si trunchiarea acestuia
mycursor.execute("CREATE DATABASE IF not exists recensamant")
mycursor.execute("use recensamant")
mycursor.execute("CREATE table if not exists datele (province varchar(255),"
                 "population int(11), area real)")
mycursor.execute("truncate table datele")

#   Inserarea datelor din conditie
sql = "insert into datele (province, population, area) values (%s, %s, %s)"
values = [
    ('Newfoundland and Labrador', '512930', '370501.69'),
    ('Prince Edward Island', '135294', '5684.39'),
    ('Nova Scotia', '908007', '52917.43'),
    ('New Brunswick', '729498', '71355.67'),
    ('Quebec', '7237479', '1357743.08'),
    ('Ontario', '11410046', '907655.59'),
    ('Monitoba', '1119583', '907655.59'),
    ('Saskatchewan', '978933', '586561.36'),
    ('Alberta', '2974807', '639987.12'),
    ('British Columbia', '3907738', '926492.48'),
    ('Yukon Territory', '28674', '474706.97'),
    ('Northwest Territories', '37360', '1141108.37'),
    ('Nunavut', '26745', '1925460.18')
]
mycursor.executemany(sql, values)
#   Salvarea modificarilor in baza de date
mydb.commit()

#   Afiseaza toate datele
mycursor.execute("select * from datele")
print("Toate datele din tabelul datele:")
print_cursor(mycursor)

#   Afizeaza doar populatia
mycursor.execute("select population from datele")
print("\nPopulatiile din tabelul datele:")
print_cursor(mycursor)

#   Afiseaza provinciile unde populatia este mai mica de 1000000
mycursor.execute("select province, population from datele where population < 1000000")
print("\nProvinciile unde populatia este mai mica de 1000000 de locuitori:")
print_cursor(mycursor)

#   Afiseaza provinciile unde populatia este mai mica de 1000000 sau mai mare de 5000000
mycursor.execute("select province, population from datele where"
                 "(population > 5000000) or"
                 "(population < 1000000)")
print("\nProvinciile unde populatia este mai mica de 1000000 de locuitori sau mai mare de 5000000:")
print_cursor(mycursor)

#   Afiseaza provinciile unde populatia este mai mica de 5000000 sau mai mare de 1000000
mycursor.execute("select province, population from datele where"
                 "(population < 5000000) and"
                 "(population > 1000000)")
print("\nProvinciile unde populatia este mai mica de 5000000 de locuitori sau mai mare de 1000000:")
print_cursor(mycursor)


#   Afiseaza provinciile aria carora este mai mare de 200000
mycursor.execute("select province, area from datele where area > 200000")
print("\nProvinciile aria carora este mai mare de 200000:")
print_cursor(mycursor)

#   Afiseaza provinciile impreuna cu densitatea (populatia / aria)
mycursor.execute("select province, population / area from datele")
print("\nProvinciile impreuna cu densitatea lor:")
print_cursor(mycursor)
