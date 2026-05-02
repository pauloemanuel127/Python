import tkinter as tk
from tkinter import PhotoImage

#Instanciar a janela
#janela = tk.Tk() define a variavel janela como uma pagina
janela = tk.Tk()
#janela.title() dá um titulo a janela
janela.title("Teste1")
#janela.geometry() define o tamanho e posição da janela
janela.geometry("1200x700+20+20")

#Criar e posicionar um label com a mensagem
lblMsg = tk.Label(janela, text="Hello World!")
lblMsg.pack()

imagem = PhotoImage(file="image_1.png")

lblimg = tk.Label(
    janela,
    image=imagem
)

lblimg.pack(pady=20)
#Exibir a janela
janela.mainloop()
