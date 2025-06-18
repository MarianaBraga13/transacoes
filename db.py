import sqlite3

def conectar():
    return sqlite3.connect()

def criar_tabelas():
    conn = conectar()
    cursor = conn.conectar()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clientes (
                    id_clientes INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    senha TEXT NOT NULL,       
                    patrimonio REAL NOT NULL   
                   
                    );
            """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS transacoes (
                    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER,
                    capital REAL NOT NULL,
                    depositos REAL NOT NULL,
                    transferencias REAL NOT NULL,
                    retiradas REAL NOT NULL,
                    data TEXT NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES (id_clientes)
                    FOREIGN KEY (capital) REFERENCES (patrimonio)                   
                    );
            """)