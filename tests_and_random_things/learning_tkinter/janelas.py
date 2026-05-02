import tkinter as tk

janela = tk.Tk()
janela.title("Janela Principal")
janela.geometry("500x400+200+100")

#janela.config() Permite alterar algumas configurações/caracteristicas da janela
#Nessa caso bg se refere a background e está definindo a cor para lightblue
#As cores podem ser encontradas na documentação ou definidas por rgd
janela.config(bg="lightblue")

#janela.minsize ou janela.maxsize definem tamanho para a janela,
#minsize define o tamanho minimo,
#maxsize define o tamanho maximo

#janela.maxsize(800,600)
#janela.minsize(300,200)

#janela.resizable() define se o formato/tamanho da janela é redimensionavel
#Recebe entradas booleanas
#janela.resizable(True,True)

#janela.state() permite a janela aparecer em tela cheia, ou outros formatos
#nesse caso está se colocando em tela cheia
#janela.state("zoomed")

#janela.attributes() permite alterar atributos na janela como sua trasparencia
#nesse caso a trasparencia é alterada
#janela.attributes("-alpha", 0.6)

#janela.iconbitmap() altera o icone da janela para um icone presente na maquina
janela.iconbitmap('jajaken.ico')

janela.mainloop()