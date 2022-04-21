import mysql.connector

connection=mysql.connector.connect(host='localhost',
                                   user='root',passwd='root',database='test',
                                   auth_plugin='mysql_native_password')
cursor=connection.cursor()#helps to use multiple in one connection
sql='insert into test_db values(%s,%s,%s)'
val=[('4','Likith','SIT'),('5','',''),('6','','')]
rows=cursor.executemany(sql,val)
#dbs=cursor.fetchall() here we are storing the data in some memory and then looping over it
#print(dbs)
connection.commit()
print(cursor.rowcount)
connection.close()