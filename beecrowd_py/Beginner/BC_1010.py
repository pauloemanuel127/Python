#Resolução do exercicio BC 1010 - Calculo simles

#Entrada de dados
#.split() é um método de string responsavel por dividir as informações por meio de um argumento
#o argumento pode ser uma (,); (.) ou outras formas
# caso venha sem argumento, será considerada a barra de espaço

a = input().split() 
b = input().split()

#Processamento dos dados
#A variavel a e b armazenam a string enviada
#O .split divide a string em elementos e
#O uso do [1], [2] são os indices que indicam qual elemento da string será utilizado

c = int(a[1])*float(a[2])
d = int(b[1])*float(b[2])
e = c+d

#Saída de dados

print(f'VALOR A PAGAR: R$ {e:.2f}')