import sqlite3

conexao = sqlite3.connect ('todocli')
cursor = conexao.cursor ()


cliente_id = input ("qual ID  que deseja alterar ?")
nome = input ("digite o novo nome:")
cpf = input ("digite o novo CPF:")
sql_update = ' UPDATE nomecliente SET nome = ? , cpf = ? where id =?'
valores = [nome,cpf,cliente_id]
cursor.execute (sql_update,valores)

atividade_id = input ("qual ID da atividade que deseja alterar ?")
atividade = input ("digite a atividade a ser alterada")
sql_update2 = ' UPDATE atividade SET atividade_academia =? where id =?'
valores = [atividade_id,atividade]
cursor.execute (sql_update2,valores)

conexao.commit ()
conexao.close ()