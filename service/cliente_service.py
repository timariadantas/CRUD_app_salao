from repository import cliente_repository
from domain.cliente import Cliente

# Camada de serviço , chama as funções do repositorio.
# Funções 

def cadastra_cliente(nome, telefone, servico):
    if not nome or not telefone or not servico:
        raise ValueError("Nome, telefone e serviço , são obrigatórios")
    cliente = Cliente(id=None, nome=nome, telefone=telefone, servico=servico)
    cliente_repository.adicionar_cliente(cliente)
    
def ver_clientes():
    return cliente_repository.listar_clientes()

def remover_cliente(id):
    cliente_repository.deletar_cliente(id)
    

    