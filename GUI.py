from tkinter import *
from tkinter import messagebox

def redimencionar():
    escala = entry2.get()
    if not escala:
        messagebox.showerror('escala', 'insira números inteiros ou decimais')

root = Tk()
root.configure(bg='cyan4')


label = Label(root, text='Redimencionador de imagens', bg='cyan4', fg='cyan', font=('Areal', 20))
label.place(x=500, y=20)

label = Label(root, text='Escolha uma imagem: ', font=('Areal', 20), bg='cyan4', fg='white')
label.place(x=300, y=200)
entry1 = Entry(root, font= ('Areal', 20))
entry1.place(x= 600, y=200)

label = Label(root, text='Escolha uma escala: ', font=('Areal', 20), bg='cyan4', fg='white')
label.place(x=310, y=240)
entry2 = Entry(root, font= ('Areal', 20))
entry2.place(x= 600, y=250)

button = Button(root, text= 'Redimencionar', bg='cyan4', font=('Areal', 15), fg='cyan', bd=5)
button.place(x=500, y=500)

root.mainloop()