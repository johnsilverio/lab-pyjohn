# Bem vindos a minha mercearia! Aproveite
# Esse é um dicionário de produtos com códigos e preços
produtos = {
    101: {"nome": "Arroz (1 kg)", "preco": 5.99},
    102: {"nome": "Feijão (1 kg)", "preco": 4.49},
    103: {"nome": "Macarrão (500g)", "preco": 2.29},
    104: {"nome": "Açúcar (1 kg)", "preco": 3.99},
    105: {"nome": "Sal (1 kg)", "preco": 1.99},
    106: {"nome": "Óleo de cozinha (1 litro)", "preco": 7.99},
    107: {"nome": "Leite (1 litro)", "preco": 3.49},
    108: {"nome": "Ovos (dúzia)", "preco": 5.29},
    109: {"nome": "Pão de forma", "preco": 3.79},
    110: {"nome": "Manteiga (200g)", "preco": 4.99},
    111: {"nome": "Queijo (250g)", "preco": 6.49},
    112: {"nome": "Presunto (250g)", "preco": 7.99},
    113: {"nome": "Frango (1 kg)", "preco": 9.99},
    114: {"nome": "Carne moída (1 kg)", "preco": 15.99},
    115: {"nome": "Peixe (500g)", "preco": 12.49},
    116: {"nome": "Macarrão instantâneo", "preco": 1.29},
    117: {"nome": "Molho de tomate (500g)", "preco": 2.99},
    118: {"nome": "Refrigerante (2 litros)", "preco": 4.49},
    119: {"nome": "Água mineral (1,5 litro)", "preco": 1.99},
    120: {"nome": "Suco de laranja (1 litro)", "preco": 6.99},
    121: {"nome": "Café (250g)", "preco": 8.99},
    122: {"nome": "Chá (caixa de 25 sachês)", "preco": 3.99},
    123: {"nome": "Bolachas (pacote)", "preco": 2.79},
    124: {"nome": "Chocolate (barra)", "preco": 3.49},
    125: {"nome": "Batata (1 kg)", "preco": 2.99},
    126: {"nome": "Cenoura (1 kg)", "preco": 2.49},
    127: {"nome": "Maçã (1 kg)", "preco": 4.99},
    128: {"nome": "Banana (1 kg)", "preco": 3.49},
    129: {"nome": "Tomate (1 kg)", "preco": 5.99},
    130: {"nome": "Alface (unidade)", "preco": 1.79},
}

carrinho = {}
# Função que adiciona o meu produto no carrinho
def adicionar_produto():
    while True:
        print("\nOpções de adicionar produto:")
        print("1. Digitar código do produto")
        print("2. Voltar ao menu principal")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            codigo_produto = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a quantidade: "))
            if codigo_produto in produtos:
                produto = produtos[codigo_produto]["nome"]
                if codigo_produto in carrinho:
                    carrinho[codigo_produto] += quantidade
                else:
                    carrinho[codigo_produto] = quantidade
                print(f"{quantidade} {produto} adicionado(s) ao carrinho.")
            else:
                print("Produto não encontrado.")
        elif escolha == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para calcular o total
def calcular_total():
    total = 0
    for codigo_produto, quantidade in carrinho.items():
        preco_unitario = produtos[codigo_produto]["preco"]
        total += preco_unitario * quantidade
    return total

# Função que exibe a lista de produtos
def exibir_lista_de_produtos():
    print("\nLista de Produtos:")
    for codigo, info in produtos.items():
        print(f"{codigo}: {info['nome']} - R${info['preco']:.2f}")

# Função principal
while True:
    print("\nBem-vindo a Mercearia do John!")
    print("\nMenu Principal:")
    print("\n1. Adicionar Produto ao Carrinho")
    print("2. Calcular Total")
    print("3. Exibir Produtos")
    print("4. Sair")
    
    escolha_principal = input("Escolha uma opção: ")
    
    if escolha_principal == "1":
        adicionar_produto()
    elif escolha_principal == "2":
        total = calcular_total()
        print(f"Total a pagar: R${total:.2f}")
    elif escolha_principal == "3":
        exibir_lista_de_produtos()
    elif escolha_principal == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")