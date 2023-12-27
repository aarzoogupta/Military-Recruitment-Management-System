#mysql-python connectivity
import mysql.connector as my
db=my.connect(host="localhost",user="root",passwd="root1")
cur=db.cursor()
cur.execute("create database IF NOT EXISTS shopping_mall")
cur.execute("use shopping_mall")
cur.execute("create table IF NOT EXISTS shops(shop_id varchar(5) primary key not null, shop_name varchar(20), shop_owner varchar(20), date_of_opening date)")
cur.execute("insert into shops values('A12','BATA','RAJEEV SHARMA','2022-02-01')")
cur.execute("insert into shops values('A13','VENUS STEPS','KAVITA GUPTA','2021-02-14')")
cur.execute("select * from shops")
x=cur.fetchall()
print(x)

db.commit()
db.close()