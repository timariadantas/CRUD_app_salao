from service import cliente_service

def menu():  # sourcery skip: avoid-builtin-shadow
    while True:
        print("\n ------Salão Aline Hair -----")
        print("1 -> Cadastar Cliente ")
        print("2 -> Listar todos os Clientes Cadastrados")
        print("3 -> Excluir Cliente")
        print("4 -> Sair ")
        opcao = input("Digite a opção desejada \n" )
        
        
        if opcao == "1":
            nome = input("Nome do Cliente \n")
            telefone = input("Telefone do Cliente: \n")
            print("Qual servico deseja ? \n")
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
                cliente_service.cadastra_cliente(nome, telefone, servico)
                print("Cliente cadastrado com sucesso.")
            except ValueError as e:
                print("Erro:", e)
        elif opcao =="2":
            clientes = cliente_service.ver_clientes()
            for c in clientes:
                print(f"ID : {c.id} | Nome: {c.nome} | Telefone: {c.telefone} | Serviço: {c.servico}")
                
        elif opcao == "3":
            id = input("ID do cliente para deletar:")
            cliente_service.removendo_cliente(id)
            print("Cliente foi removido!")
            
        elif opcao == "4":
            break
        else:
            print("Opçãp invalida, Tente novamente.")
        
                
                
if __name__ == "__main__":
   menu()