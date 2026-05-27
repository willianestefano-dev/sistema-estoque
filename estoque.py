import json

#carregamento produto-------------------------------
def carregar_produtos():

    try:
        with open("produto.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
#salvar---------------------------------------------

def salvar_produto(lista):

    with open("produto.json", "w") as arquivo:
        json.dump(lista, arquivo, indent=4)

#validar nome - adicionar---------------------------------------

def validar_nome(nome):

    if not nome.strip():
        return "Campo nome vazio, cadastro cancelado tente novamente"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras, cadastro cancelado tente novamente"
    
    return "ok"

#validar nome - busca---------------------------------------

def validar_busca(nome):

    if not nome.strip():
        return "Campo nome vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#validar nome - alterar------------------------------------

def validar_alterar(nome):

    if not nome.strip():
        return "Campo nome vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#validar novo_nome - altera--------------------------

def validar_novo_nome(novo_nome):

    if not novo_nome.strip():
        return "Campo nome vazio, alterar nome cancelado"
    
    if not novo_nome.replace(" ","").isalpha():
        return "Apenas letras, alterar nome cancelado"
    
    return "ok"

#validar nome - remover-----------------------------

def validar_nome_remover(nome):

    if not nome.strip():
        return "Campo nome vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#menu------------------------------------------------

while True:

    print("------------Menu-----------")
    print("1 - Adicionar produtos")
    print("2 - Listar produtos")
    print("3 - Buscar produtos")
    print("4 - Alterar produtos")
    print("5 - Remover produtos")
    print("6 - Sair")

    opcao = input("Digite sua escolha: ")
    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Escolha invalida, tente novamente")

#Adicionar produto-----------------------------------

    if opcao == "1":

        nome = input("Digite o nome do produto: ").lower()
        #validar nome
        validar = validar_nome(nome)
        if validar != "ok":
            print(validar)
            continue
        #validar qtd
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade < 0:
                print("quantidade incorreta")
                continue
            
        except ValueError:
            print("Apenas numeros, cadastro cancelado tente novamente")
            continue

        #validar preço
        try:
            preco = float(input("Digite o preço do produto: "))            
            if preco < 0:
                print("Preço incorreta")                    
                
        except ValueError:
            print("Apenas numeros, cadastro cancelado tente novamente")
            continue

        #adicionar
        lista = carregar_produtos()
        produto = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
        lista.append(produto)
        salvar_produto(lista)

        print("Pruduto adicionado")

#listar----------------------------------------------

    elif opcao == "2":

        lista = carregar_produtos()

        if not lista:
            print("Lista de produtos vazia")
        else:
            for i, produto in enumerate(lista, start=1):
                print(f"{i}. Nome: {produto['nome']} - Quantidade: {produto['quantidade']} - Preço R$: {produto['preco']}")
    
#buscar-----------------------------------------------

    elif opcao == "3":

        lista = carregar_produtos()
        encontrou = False
        #validar nome--------------------------------
        nome = input("Buscar qual produto: ").lower()
        validar = validar_busca(nome)
        if validar != "ok":
            print(validar)
            continue
        #buscar
        for produto in lista:
            if produto['nome'] == nome:
                encontrou = True
                print(f"Nome: {produto['nome']} - Quantidade: {produto['quantidade']} - Preço R$: {produto['preco']}")
        if not encontrou:
            print("Produto não cadastrado")

#alterar produto--------------------------------------

    elif opcao == "4":

        lista = carregar_produtos()
        encontrou = False
        #validar nome------------------------------------------------
        nome = input("Digite o produto que deseja alterar: ").lower()
        validar = validar_alterar(nome)
        if validar != "ok":
            print(validar)
            continue

        for produto in lista:
            if produto['nome'] == nome:
                encontrou = True
                print(f"Nome: {produto['nome']} - Quantidade: {produto['quantidade']} - Preço R$: {produto['preco']}")
                confirmar = input("Realmente deseja alterar o produto? (s/n): ").lower()

                if confirmar == "s":
                    escolha = input("O que deseja alterar: Nome(n) - Qtd(q) - Preço(p): ").lower()

                    if escolha == "n":
                        #alteracao nome e validar nome
                        novo_nome = input("Digite o novo nome: ").lower()
                        validar = validar_novo_nome(novo_nome)
                        if validar != "ok":
                            print(validar)
                            continue

                        produto['nome'] = novo_nome
                        salvar_produto(lista)

                        print("Nome do produto alterado")
                    
                    elif escolha == "q":
                        #alteracao quantidade e validar quantidade
                        try:
                            nova_quantidade = int(input("Digite a quantidade: ")) 
                            if nova_quantidade < 0:
                                print("Quantidade não pode ser negativa")    
                                continue

                        except ValueError:
                            print("Apenas numeros")                  
                        produto['quantidade'] = nova_quantidade
                        salvar_produto(lista)

                        print("Quantidade alterada")

                    elif escolha == "p":
                        #Alteracao preço e validar preco
                        try:
                            novo_preco = float(input("Digite novo preço: "))
                            if novo_preco < 0:
                                print("Preço incorreta")   
                                continue

                        except ValueError:
                            print("Apenas preços ex: R$ 10.00")                       

                        produto['preco'] = novo_preco
                        salvar_produto(lista)

                        print("Preço alterado")
                
                else:
                    print("Alterar produto cancelado")

        if not encontrou:
            print("Produto não encontrado")    

#remover---------------------------------------------------

    elif opcao == "5":

        lista = carregar_produtos()
        encontrou = False
        #validar nome
        nome = input("Digite o nome do produto que deseja remover: ").lower()
        validar = validar_nome_remover(nome)
        if validar != "ok":
            print(validar)
            continue

        for produto in lista:
            if produto['nome'] == nome:
                encontrou = True

                print(f"Nome: {produto['nome']} - Quantidade: {produto['quantidade']} - Preço R$: {produto['preco']}")
                confirmar = input("Realmente deseja remover este produto? (s/n): ").lower()

                if confirmar == "s":
                    lista.remove(produto)
                    salvar_produto(lista)

                    print("Produto removido")
                    break
                
                else:
                    print("Remover produto cancelado")

        if not encontrou:
            print("Produto não cadastrado")

#sair--------------------------------------------------------

    elif opcao == "6":
        print("Saindo do sistema.........")
        break

                        





       


