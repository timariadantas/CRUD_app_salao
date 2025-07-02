from database.database import conexao_bd
from domain.cliente import Cliente

# -- Funções

def adicionar_cliente(cliente):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO clientes (nome, telefone, servico) VALUES (? ,? ,?)',(cliente.nome, cliente.telefone, cliente.servico))
    conexao.commit()
    conexao.close()
    
def listar_clientes():
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM clientes')
    rows = cursor.fetchall()
    conexao.close()
    
    clientes = []
    for row in rows:
        cliente = Cliente(
            id=row[0],
            nome=row[1],
            telefone=row[2],
            servico=row[3]
        )
        clientes.append(cliente)
        
    return clientes

def deletar_cliente():
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    
def cliente_id(id):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute('SELECT FROM clientes WHERE id = ?', (id,))
    row = cursor.fetchone()
    conexao.close()
    
    if row:
        return Cliente(id=row[0], nome=row[1], telefone=row[2], servico=row[3])
    return None

