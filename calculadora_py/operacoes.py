#Modulo responsavel pelas operações matematicas da calculadora e seu historico

list_historico = []

def soma(X,Y):
    valor = X+Y
    operacao_historico = str(f'{X} + {Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def subtracao(X,Y):
    valor = X-Y
    operacao_historico = str(f'{X} - {Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def multiplicacao(X,Y):
    valor = X*Y
    operacao_historico = str(f'{X} x {Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def divisao(X,Y):
    #Essa cadeia de condicional alinhada serve para caso onde o usuario tente fazer divisão por 0 e o codigo não falhe
    if X == 0  and Y == 0:
        operacao_historico = str('0/0 = Indeterminação')
        list_historico.append(operacao_historico)
        return operacao_historico

    elif Y == 0:
        operacao_historico = str(f'{X}/0 = Indefinido')
        list_historico.append(operacao_historico)
        return operacao_historico
    else:
        valor = X/Y
        operacao_historico = str(f'{X}/{Y} = {valor:.2f}')
        list_historico.append(operacao_historico)
        return operacao_historico
    
def potencia(X,Y):
    valor = X**Y
    operacao_historico = str(f'{X}^{Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def raiz(X,Y):
    valor = Y**(1/X)
    operacao_historico = str(f'{round(X)}\\/{Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def salvar_historico():

    #Usando o list_historico[-10:] para puxar somente as ultimas 10 operações, é utilizada a função do python open,
    #Que permite a interação entre o codigo e arquivos na memoria estatica,
    #Por meio disso é criado um arquivo.txt que armazena a list_historico[-10:], utilizando o metodo de descriptografia utf-8 para os textos
    historico = list_historico[-10:]
    with open("historico.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== HISTÓRICO DA CALCULADORA ===\n")
        for i in historico:
            arquivo.write(i + "\n")

def carregar_historico():
    #O global avisa que vamos mexer na lista inicial lá do topo
    global list_historico

    try:
        #Lê todas as linhas, remove o titulo e os espaços em branco
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            #Ignora a primeira linha do arquivo que é o titulo
            list_historico = [linha.strip() for linha in linhas if "===" not in linha]

    except FileNotFoundError:
        #Caso o arquivo ainda não exista ele não faz nada
        list_historico = []