import sqlite3

#Criando conexao com banco de dados , retorna a conexap para uso em consultas
def conexao_bd():
    conexao = sqlite3.connect('salao_aline_bd')
    return conexao

# Função criar tabelas , cursor que executa comandoS SQL , salva e fecha a conexao.
def create_tables():
    conexao = conexao_bd()
    cursor = conexao.cursor()
    
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            servico TEXT NOT NULL
        )
    
    """
    )
    
    conexao.commit()
    conexao.close()
    

create_tables()