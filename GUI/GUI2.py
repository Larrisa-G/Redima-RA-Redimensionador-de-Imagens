import customtkinter as ct
 
def initial(root):
    e1 = ct.CTkEntry(root, placeholder_text="escala")
    e1.pack()


def main():
    root = ct.CTk()
    root.title("Recurção aninhada")
    root.geometry("600x400")
    root.configure()

    initial(root)

    root.mainloop()

main()