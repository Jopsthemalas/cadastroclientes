import sqlite3

conexao= sqlite3.connect ('todocli')
cursor=conexao.cursor ()

sql1='''CREATE TABLE nomecliente (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
    cpf TEXT(14) NOT NULL,
 CONSTRAINT cliente_UN UNIQUE (cpf)
    );'''
cursor.execute (sql1)

sql2='''CREATE TABLE atividade (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	atividade_academia TEXT,
	CONSTRAINT atividade_FK FOREIGN KEY (atividade_academia) REFERENCES nomecliente(id)
);'''

cursor.execute (sql2)

sql3 = '''CREATE TABLE exercicios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
atividade_id INTEGER NOT NULL ,
exercicios TEXT (100),
quantidade INTEGER,
CONSTRAINT atividade_FK FOREIGN KEY (atividade_id) REFERENCES atividade(id)
); '''
cursor.execute (sql3)

sql4='''CREATE TABLE checklist (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "data" TEXT NOT NULL,
    concluido_id TEXT,
 CONSTRAINT concluido_id_FK FOREIGN KEY (concluido_id) REFERENCES nomecliente(id)
    );'''

cursor.execute (sql4)



conexao.commit ()

conexao.close ()
