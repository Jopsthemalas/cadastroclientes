import sqlite3
conexao= sqlite3.connect ('todocli')
cursor=conexao.cursor ()


cliente_id = input("qual ID cliente deseja excluir ?")
sql_delete = 'Delete from nomecliente where id =?'
valores = (cliente_id)
cursor.execute (sql_delete,valores)

atividade = input("qual ID  atividade  deseja excluir ?")
sql_delete2 = 'Delete from atividade where id =?'
valores = (atividade)
cursor.execute (sql_delete2,valores)


conexao.commit ()
conexao.close