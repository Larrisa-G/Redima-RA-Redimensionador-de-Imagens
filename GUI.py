import tkinter as tk

cor0 = 'white'
cor1 = 'cyan'
cor2 = 'cyan4'

root = tk.Tk()
root.geometry("700x500")
root.title("Redimencionador de imagens")

# Criando alguns widgets
label1 = tk.Label(root, text='Redimencionador de imagens', bg=cor2, fg=cor1, font=('Areal', 20))

button1 = tk.Button(root, text='Escolha uma imagem',bg=cor0, font= ('Areal', 15), fg=cor2)

entry = tk.Entry(root, text='Escala',bg=cor0, font= ('Areal', 15), fg=cor2)

button = tk.Button(root, text= 'Redimensionar', bg=cor2, font=('Areal', 15), fg=cor1, bd=5)

# Usando pack() para posicionar os widgets com espaçamento
label1.pack(padx=10, pady=40)
button1.pack(padx=10, pady=10, side=tk.LEFT)
entry.pack(padx=10, pady=10, side=tk.RIGHT)
button.pack(padx=10, pady=10)

root.mainloop()
