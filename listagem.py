import sqlite3

conexao = sqlite3.connect ('todocli')
cursor = conexao.cursor ()

sql= 'select * from nomecliente'

cursor.execute(sql) 
result = cursor.fetchall() 
for row in result: 
    print(row) 
    print("\n") 


    sql2= 'select * from atividade'

cursor.execute(sql2) 
result = cursor.fetchall() 
for row in result: 
    print(row) 
    print("\n") 


    sql3= 'select * from exercicios '

cursor.execute(sql3) 
result = cursor.fetchall() 
for row in result: 
    print(row) 
    print("\n") 