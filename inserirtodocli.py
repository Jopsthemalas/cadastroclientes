import sqlite3
import datetime

conexao= sqlite3.connect ('todocli')
cursor=conexao.cursor ()

print ("insira o nome e a atividade da academia:")

nome = input ("qual seu nome?")
cpf = input ("qual cpf?")
sql= 'insert into nomecliente (nome,cpf) values (?,?);'
valores = [nome,cpf]
cursor.execute (sql,valores)

atividade= input ("qual atividade?")
sql_atividade = 'insert into atividade (atividade_academia)values (?);'

valores = [atividade]
cursor.execute (sql_atividade,valores)

print ('ID do cliente:',cursor.lastrowid)
atividade_id = cursor.lastrowid
quantidade_ex= input ("quantos exercicios deseja adicionar ?")
quantidade_ex = int(quantidade_ex)
for i in range (quantidade_ex) :
    exercicio = input ("qual o exercicio?")
    quantidade = input ("qual a quantidade do repetiçao ?")
    quantidade = int (quantidade)
    
    sql_ex = '''
    INSERT INTO exercicios 
    (atividade_id,exercicios,quantidade) values (?,?,?);'''
    
    valores = [atividade_id,exercicio,quantidade,]
cursor.execute (sql_ex,valores)

data = datetime.date.today()

concluido_id = input ("conclui a atividade hoje ?")
sim = ("sim")

if concluido_id == sim:

    sql_ck = 'insert into checklist (data,concluido_id)values (?,?)'

else :
    print("atividade nao concluida")

valores = [data,concluido_id]

cursor.execute (sql_ck,valores)


conexao.commit ()
conexao.close ()

