from tkinter import*
from tkinter.simpledialog import*
Lbl=Label(text='Hello user')
Lbl.pack()
mas=[]
def Klubnika():
    for i in range(5):
        a = int(askstring('1,2,3,4,5','mas['+str(i)+']='))
    for i in range(5):
        Lbox.insert(END,mas[i])
from tkinter import*
window=Tk()
mas=[]
Lbl=Label(text='Write a massive')
Lbl.pack()
Ent=Entry()
Ent.pack()
Btn=Button(text='Write a massive')
Btn.pack()
Lbox=Listbox()
Lbox.pack()
mas=[]
def Malinka():
    a = Ent.get()
    mas = a.split()
    for i in mas:
        Lbox.insert(END,in)
