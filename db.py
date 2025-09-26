import mysql.connector
from datetime import datetime
try:
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'itzmcs2004',
        database = 'testdatabase'
    )
    print('Connection successful')
except mysql.connector.Error as mce:
    print('Error : ',mce)

my_cursor = db.cursor()
# my_cursor.execute(
#     'CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)'
#     )

# my_cursor.execute(
#     'CREATE TABLE Test (Id int PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50), created datetime,gender ENUM("M","F","O"))'
# )

# my_cursor.execute('INSERT INTO Person (name,age) VALUES (%s,%s)',('Job',24))
# db.commit()

my_cursor.execute('INSERT INTO Test (name,created,gender) VALUES (%s,%s,%s)',('Maxwell',datetime.now(),'M'))
db.commit()

my_cursor.execute('ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL')
# my_cursor.execute('SELECT Id, name FROM Test WHERE gender = "F" ORDER BY Id DESC')
# for rows in my_cursor:
#     print(rows)

# my_cursor.execute('DESCRIBE Test')
# for rows in my_cursor:
#     print(rows)