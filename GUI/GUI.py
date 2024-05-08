from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image
import easygui as eg
from main import escalar_imagem

def selecionar_imagem () :
    global caminho_imagem
    global largura
    global altura

    caminho_imagem = eg.fileopenbox()

    if caminho_imagem:
        imagem = Image.open(caminho_imagem)
        largura, altura = imagem.size
        imagem.close()
        print(caminho_imagem)
        print(largura)
        print(altura)
        return str(caminho_imagem), int(largura), int(altura)
    else:
        return None, None, None

#variáveis
cor0 = 'white'
cor1 = 'cyan'
cor2 = 'cyan4'



#criação dos widgets
def initial(root):
    frame_top = tk.Frame(root)
    frame_bottom = tk.Frame(root)
    frame_right = tk.Frame(root)
    frame_left = tk.Frame(root)

    label = Label(root, text='Redimencionador de imagens', bg=cor2, fg=cor1, font=('Areal', 20))
    button1 = Button(root, text='Escolha uma imagem',bg=cor0, font= ('Areal', 14), fg=cor2, command=selecionar_imagem)
    input = Entry(root, font= ('Areal', 14), fg=cor2)
    button = Button(root, text= 'Redimensionar', bg=cor2, font=('Areal', 13), fg=cor1, bd=5, command=lambda:escalar_imagem(caminho_imagem, largura, altura, input.get()))

    #mostra na tela
    frame_top.pack(padx=10, pady=20, side=tk.TOP)
    frame_bottom.pack(padx=10, pady=40, side=tk.BOTTOM)
    frame_right.pack(padx=15, pady=0, side=tk.RIGHT)
    frame_left.pack(padx=15, pady=0, side=tk.LEFT)

    label.pack(padx=5, pady=5)
    button1.pack(padx=1, pady=5, side=tk.LEFT, anchor=tk.CENTER)
    input.pack(padx=1, pady=5, side=tk.RIGHT, anchor=tk.CENTER)
    button.pack(side=tk.BOTTOM, anchor=tk.CENTER)



#configurações da janela


def main():
    root = tk.Tk()
    root.title("RedimaRA - Redimensionador de Imagens")
    root.geometry("600x400")
    root.configure(bg=cor2)

    initial(root)

    root.mainloop()

main()