import mysql.connector
mydb=mysql.connector.connect(
  host='localhost',
  username='root',
  password=''
)
mycursor=mydb.cursor()
mycursor.execute('create database  information')

#create table
mydb=mysql.connector.connect(
  host='localhost',
  username='root',
  password='',
  database='information'
)
mycursor=mydb.cursor()
mycursor.execute('create table usersinform( id int auto_increment primary key   ,firstname varchar(255),lastname varchar(255),password varchar(100))')
#alter table
mydb=mysql.connector.connect(
  host='localhost',
  username='root',
  password='',
  database='information'
)
mycursor=mydb.cursor()
mycursor.execute('alter table usersinform add column email varchar(100)')
