from random import choice
from tkinter import *

lista = []
nm_sorteados = 0


def gerarLista():
    global lista, nm_sorteados
    try:
        sorteados.delete(0, END)
        nm_sorteados = 0
        start = int(valor_inicial.get())
        end = int(valor_final.get()) + 1
        lista = [*range(start, end)]
        restam.set(f"Restam:           {len(lista)}")
        ja_sorteados.set(f"Sorteados:       {nm_sorteados}")
    except:
        restam.set("Valores Invalidos")
        ja_sorteados.set("")

def inserirItem():
    global lista, nm_sorteados
    try:
        item = choice(lista)
        sorteados.insert(0, item)
        lista.pop(lista.index(item))
        nm_sorteados += 1
        restam.set(f"Restam:           {len(lista)}")
        ja_sorteados.set(f"Sorteados:       {nm_sorteados}")
        ultimo.set(f"Último Número Sorteado: {item}")
    except IndexError:
        nm_sorteados = 0
        restam.set("Fim")
        ja_sorteados.set("")
root = Tk()
root.geometry(f"560x480+{int((root.winfo_screenwidth() - 560)/2)}+{int((root.winfo_screenheight() - 480)/2)}")
root.title("Sorteio de Números")

frm = Frame(root)
frm.place(x=420,y=6)

scrollbar = Scrollbar(frm)
scrollbar.pack(side=RIGHT, fill=Y)

sorteados = Listbox(frm, width=13,height=23,font=('arial',12,'bold'))
sorteados.pack()

sorteados.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=sorteados.yview)


valor_inicial = Entry(width=7,font=('arial',20,'bold'))
valor_inicial.place(x=80, y=70)

valor_final = Entry(width=7,font=('arial',20,'bold'))
valor_final.place(x=230, y=70)


Button(text='Iniciar',width=7,font=('arial',18,'bold'), command=gerarLista).place(x=150,y=150)
Button(text='Sortear número',width=15,font=('arial',18,'bold'), command=inserirItem).place(x=100,y=370)

ja_sorteados = StringVar()
ja_sorteados.set("Sorteados: ")
Label(textvariable=ja_sorteados,font=('arial',15,'bold')).place(x=80,y=220)


restam = StringVar()
restam.set("Restam: ")
Label(textvariable=restam,font=('arial',15,'bold')).place(x=80,y=260)


ultimo = StringVar()
ultimo.set("Último Número Sorteado: ")
Label(textvariable=ultimo,font=('arial',15,'bold'),fg='red').place(x=30,y=440)


root.mainloop()



