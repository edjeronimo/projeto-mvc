import sqlite3 as db

class Conexao:
    
    def __init__(self):
        self.conn = db.connect('model/escola.db')
        self.criarTabelas()
    def criarTabelas(self):
        
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS aluno(
                id integer primary key autoincrement,
                nome varchar(100) not null,
                email varchar(150) not null,
                senha text
            )
        """)
        
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS professor(
                x ...
            ),
            FOREIGN KEY(x) REFERENCES aluno(id)
        """)
        
Conexao()