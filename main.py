from service import cliente_service

def menu():
    while True:
        print("\n ------Salão Aline Hair -----")
        print("1 -> Cadastar Cliente")
        print("2 -> Listar todos os Clientes Cadastrados")
        print("3 -> Excluir Cliente")
        print("4 -> Sair ")
        opcao = input("Digite a opção desejada")
        
        
        if opcao == "1":
            nome = input("Nome do CLiente")
            telefone = input("Telefone do Cliente: ")
            print("Qual servico deseja ?")
            print("1- Manicure")
            print("2- Cabelereiro")
            print("3- Estética")
            servico_opcao = input ("Opção: ")
            if servico_opcao == "1":
                servico = "Manicure"
            elif servico_opcao == "2":
                servico = "Cabeleiro"
            elif servico_opcao == "3":
                servico = "Estética"
            else:
                print("Serviço inválido.")
                continue
            try:
                cliente_service.cadastrar_cliente(nome, telefone, servico)
                print("Cliente cadastrado com sucesso.")
            except ValueError as e:
                print("Erro:", e)
                
                
if __name__ == "__main__":
   menu()