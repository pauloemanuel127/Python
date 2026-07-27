#Projeto de um sistema de calculadora para realização de operações
#A logica por trás é apenas realizar calculos das 4 operações basicas, soma, subtração, multiplicação e divisão

import operacoes as op #Importando as funções para as operações e a lista com o historico
import re #Importando a biblioteca Regex

print('Bem vindo!')

#Carrega o historico para a lista
op.carregar_historico()

#O loop de while True serve para manter a calculadora em funcionamento e assim poder realizar varias operações seguidas
while True:

    print("Digite a expressão a ser calculada no seguinte formato X + Y, tendo como opção as seguintes operações:\n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão")
    print('^ para potenciação (sendo aplicado no formato X^Y)\nr para radiciação (sendo aplicado no formato XrY, sendo X o indice e Y o radicando)\nDigite:\nhist para ver o historico de operações ou exit para sair')
    entrada = input('')

    #Após a entrada ser enviada, será feita a verificação se o usuario está pedindo para realizar uma operação, sair ou ver o historico de operações

    if entrada == 'exit':
        #Aqui é realizada o fim do funcionamento do programa à pedido do usuario, 
        #A função salvar historico salva as ultimas 10 operações em um arquivo .txt
        op.salvar_historico()
        print('Obrigado por usar nossa calculadora')
        break

    elif entrada == 'hist':
        #Caso o usuario tenha digitado hist logo de começo, será printado um vazio.
        #Para cada elemento na lista e seu respectivo "valor", será impresso a posição do elemento e seu "valor".
        #O uso do op.list_historico[-10:], 
        #Define que a esse loop for vai puxar somente os ultimos 10 elementos da lista, começando pelo ultimo.
        print("=== HISTÓRICO DA CALCULADORA ===\n")
        for i, conta in enumerate(op.list_historico[-10:]):
            print(f'{i+1}. {conta}')
        _ = input('Pressione Enter para avançar')
        #Esse _ input('Pressione Enter para avançar') serve para melhorar a visualização do historico de operações

    else:
        #Caso a entrada não caia em nenhuma das duas condições anteriores,
        #Aí a entrada é transformada em seus devidos valores e é relizada a operação desejada

        #Por meio da função de procura da biblioteca Regex, é verificada a string de entrada procurando o que vai ser equivalente ao X,
        #Ao operador, e ao Y, sendo organizado por meio da procura de um numero, com ou sem . após ele, e caso tenha ponto mais numeros,
        #O operador é procurado por meio da lista oferecida, e o segundo numero da mesma forma do primeiro 
        match = re.search(r"(-?\d+\.?\d*)\s*([\+\-\*/\^r])\s*(-?\d+\.?\d*)", entrada)

        #Caso o usuario tenha digitado corretamente ele vai separar cada variavel e realizar as operações
        if match:

            X = float(match.group(1))
            operador = match.group(2)
            Y = float(match.group(3))

                #Aqui entramos exatamente na cadeia onde será realizada a verificação do operador
            if operador == '+':
                resultado = op.soma(X,Y)
                print(f'Esse é o resultado da soma: {resultado}')
                _ = input('Pressione Enter para avançar')

            elif operador == '-':
                resultado = op.subtracao(X,Y)
                print(f'Esse é o resultado da subtração: {resultado}')
                _ = input('Pressione Enter para avançar')

            elif operador == '*':
                resultado = op.multiplicacao(X,Y)
                print(f'Esse é o resultado da multiplicação: {resultado}')
                _ = input('Pressione Enter para avançar')

            elif operador == '/':
                resultado = op.divisao(X,Y)
                print(f'Esse é o resultado da divisão: {resultado}')
                _ = input('Pressione Enter para avançar')

            elif operador == '^':
                resultado = op.potencia(X,Y)
                print(f'Esse é o resultado para a potenciação: {resultado}')
                _ = input('Pressione Enter para avançar')

            elif operador == 'r':
                resultado = op.raiz(X,Y)
                print(f'Esse é o resultado da raiz {round(X)}-ésima de {Y}: {resultado}')
                _ = input('Pressione Enter para avançar')
                
            else:
                #O else está aqui para caso o usuario use um operador que não seja alguma das opções oferecidas
                print('Esse é um operador invalido, por favor tente novamente!')
                _ = input('Pressione Enter para avançar')

        #Caso tenha digitado em um formato não suportado, será apresentada essa mensagem
        else:
            print('Formato inválido! Use X + Y ou X+Y')
            _ = input('Pressione Enter para avançar')