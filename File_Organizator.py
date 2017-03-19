from tkinter import *
from tkinter import messagebox
import os
import shutil, zipfile

dest='C:/Users/Henrique/Documents/My Games'


def show_entry():
    src=str(E3.get())#Retrieves entry and converts to string
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name) and full_file_name.endswith(".txt")):
            print("iniciando copia")
            shutil.copy(full_file_name, dest)
            print("copiado com sucesso")
            messagebox.showinfo("OK", "Copiado com Sucesso")
            print("ok")

#
def show_xlsx():
    src=str(E3.get())
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name) and full_file_name.endswith(".xlsx")):
            print("iniciando copia")
            shutil.copy(full_file_name, dest)
            print("copiado com sucesso")
            print("ok")
            messagebox.showinfo("OK", "Copiado com Sucesso")
#




master = Tk()
master.geometry("750x100")
master.resizable(width=False, height=False)
master.title("File organizator")
Label(master, text="").grid(row=0,column=1)
Label(master, text="").grid(row=2,column=0)
Label(master, text="Caminho").grid(row=2,column=1)

#e1 = Entry(master)
E3 = Entry(master)
E3["width"]=100

#e1.grid(row=0, column=1)
E3.grid(row=2, column=2)



Button(master, text='Quit', command=master.quit).grid(row=0, column=0, sticky=W, pady=4)
Button(master, text='txt', command=show_entry).grid(row=3, column=2, sticky=W, pady=4)
Button(master, text='.xlsx', command=show_xlsx).grid(row=3, column=1, sticky=W, pady=4)



mainloop( )
