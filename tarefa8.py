


produtos = [
    ["1", "Caderno", 25.50],
    ["2", "Caneta", 3.00],
    ["3", "Mochila", 120.00],
    ["4", "Borracha", 2.50],
    ["5", "Estojo", 18.90]
]

while True:
    print("\n===== MENU DE PRODUTOS =====")
    print("1 - Imprimir produtos")
    print("2 - Localizar produto pelo ID")
    print("3 - Remover produto pelo ID")
    print("4 - Imprimir lista atualizada")
    print("5 - Cadastrar novo produto")
    print("6 - Alterar preço")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n===== LISTA DE PRODUTOS =====")
        for produto in produtos:
            print("ID:", produto[0])
            print("Nome:", produto[1])
            print("Preço: R$", produto[2])
            print("--------------------")

    elif opcao == "2":
        id_busca = input("Digite o ID: ")
        encontrado = False

        for produto in produtos:
            if produto[0] == id_busca:
                print("Produto encontrado:", produto)
                encontrado = True

        if encontrado == False:
            print("Produto não encontrado.")

    elif opcao == "3":
        id_busca = input("Digite o ID: ")
        i = 0

        while i < len(produtos):
            if produtos[i][0] == id_busca:
                produtos.pop(i)
                print("Produto removido!")
                break
            i = i + 1
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("\n===== LISTA ATUALIZADA =====")
        for produto in produtos:
            print("ID:", produto[0])
            print("Nome:", produto[1])
            print("Preço: R$", produto[2])
            print("--------------------")

    elif opcao == "5":
        id_produto = input("Digite o ID: ")
        nome = input("Digite o nome: ")
        preco = float(input("Digite o preço: "))

        produtos.append([id_produto, nome, preco])
        print("Produto cadastrado!")

    elif opcao == "6":
        id_busca = input("Digite o ID: ")

        for produto in produtos:
            if produto[0] == id_busca:
                produto[2] = float(input("Digite o novo preço: "))
                print("Preço alterado!")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
