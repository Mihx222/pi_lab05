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

#   Crearea, in caz ca nu exista, a tabelului capitalele
mycursor.execute("use recensamant")
mycursor.execute("CREATE table if not exists capitalele (province varchar(255),"
                 "capitala varchar(255), population int(11))")
mycursor.execute("truncate table capitalele")

#   Inserarea datelor din conditie
sql = "insert into capitalele (province, capitala, population) values (%s, %s, %s)"
values = [
    ('Newfoundland and Labrador', 'St. John\'s', '172918'),
    ('Prince Edward Island', 'Charlottetown', '58358'),
    ('Nova Scotia', 'Halifax', '359183'),
    ('New Brunswick', 'Fredericon', '81346'),
    ('Quebec', 'Quebec City', '682757'),
    ('Ontario', 'Toronto', '4682897'),
    ('Monitoba', 'Winnipeg', '671274'),
    ('Saskatchewan', 'Regina', '192800'),
    ('Alberta', 'Edmonton', '937845'),
    ('British Columbia', 'Victoria', '311902'),
    ('Yukon Territory', 'Whitehorse', '21405'),
    ('Northwest Territories', 'Yellowknife', '16541'),
    ('Nunavut', 'Iqaluit', '5236')
]
mycursor.executemany(sql, values)
#   Salvarea modificarilor in baza de date
mydb.commit()

#   Afiseaza toate datele
mycursor.execute("select * from capitalele")
print("Toate datele din tabelul capitalele:")
print_cursor(mycursor)

#   Afiseaza population provinciei si capitalei
mycursor.execute("select capitalele.province, datele.population, capitalele.population "
                 "from datele, capitalele "
                 "where datele.province = capitalele.province")
print("\nPopulatia capitalei si a provinciei:")
print_cursor(mycursor)


#   Afiseaza aria provinciilor a caror capitale au populatia mai mare de 100000
mycursor.execute("select datele.province, datele.area from datele, capitalele "
                 "where capitalele.population > 100000 "
                 "and datele.province = capitalele.province")
print("\nAria provinciilor a caror capitale au populatia mai mare de 100000")
print_cursor(mycursor)

#   Afiseaza provinciile cu densitati de populatie mai mici decat 2 si populatia capitalei
#   mai mare decat 500000
mycursor.execute("select datele.province, datele.population / datele.area "
                 "from datele, capitalele "
                 "where capitalele.population > 500000 "
                 "and datele.province = capitalele.province "
                 "and (datele.population / datele.area) < 2")
print("\nProvinciile cu densitati de populatie mai mici decat 2 si populatia capitalei mai mare decat 500000")
print_cursor(mycursor)

#   Afiseaza suprafata totala a Canadei
mycursor.execute("select sum(datele.area) from datele")
print("\nSuprafata totala a Canadei:")
print_cursor(*mycursor)


#   Afiseaza media populatiei capitalelor
mycursor.execute("select avg(capitalele.population) from capitalele")
print("\nMedia populatiilor capitalelor")
print_cursor(*mycursor)


#   Afiseaza capitala cu cea mai mica populatie
mycursor.execute("select min(population) from capitalele")
print("\nCea mai mica populatie din capitale")
print_cursor(*mycursor)

#   Afiseaza cea mai mare populatie din provincie
mycursor.execute("select max(population) from datele")
print("\nCea mai mare populatie din provincie")
print_cursor(*mycursor)

#   Afiseaza provinciile care au densitatea in jurul de 0.5
mycursor.execute("select province, population / area from datele "
                 "where round(population / area, 1) < 0.5")
print("\nProvincia cu densitatea in limita 0.5:")
print_cursor(mycursor)
