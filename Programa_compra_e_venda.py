# Criando um programa de registro de compra e venda de produtos.
# Tendo em mente que esse programa deve identificar erros de digitação!
# O programa deve também possuir um menu interativo. 

# 2º passo: Iniciando com as listas:
compras = []
vendas=[]

def registro_compra():
    produto = input("Nome do Produto: ")
# int: Representa um número inteiro, ou seja, aqui será quantidade
    qtd = int(input("Qual a Quantidade?: "))
# float: Representa um número com parte decimal, ou seja, aqui será o valor para considerarmos os centavos.
    valor = float(input("Qual o Valor do Produto?: "))
# Função Append: Adiciona elementos em uma lista
    compras.append({"produto": produto, "qtd": qtd, "valor": valor})
    print("Registro de Compra Concluído!")

def registro_venda():
    produto = input("Nome do Produto: ")
    qtd = int(input("Qual a Quantidade?: "))
    valor = float(input("Qual o Valor do Produto?: "))
    vendas.append({"produto": produto, "qtd": qtd, "valor": valor})
    print("Registro de Venda Concluído!")

def verifica_lucro():
# Função sum: Método de somatória de valores em uma sequência
    Tcompras = sum(item["qtd"]* item["valor"] for item in compras)
    Tvendas = sum(item["qtd"]* item["valor"] for item in vendas)
    lucro = Tvendas - Tcompras
# If: Código executado se a função for verdadeira
    if lucro > 0: # nesse caso queremos que a função nos dê uma resposta de acordo com o valor gerado da variável lucro
        print(f"Lucro das Vendas: R${lucro: .2f}")
# Else: Código executado quando a função anterior não for verdadeira
    else: # nesse caso se a variável lucro for negativa teremos a mensagem com o valor de prejuízo
        print(f"Prejuízo das Vendas: R${lucro: .2f}")
# .2f: Pedido de 2 casas decimais no cálculo

# 3º passo: Menu Interativo
# While True: Cria um loop infinito solicitando uma ação do usuário,
# que só será parado com a ação que indica o 'break'.

while True:
    print("MENU")
    print("1. Registrar Compra")
    print("2. Registrar Venda")
    print("3. Verificar Lucro")
    print("4. Sair")
    opcao = input("Escolha Uma Opção: ")

    if opcao == "1":
        registro_compra()

# Elif: Código executado se a primeira função for falsa e a segunda função for verdadeira
    elif opcao == "2":
        registro_venda()

    elif opcao == "3":
        verifica_lucro()

    elif opcao == "4":
        print("Você Saiu do Programa!")
        break

    else:
        print("Opção Inexistente! Escolha Outra Opção!")
