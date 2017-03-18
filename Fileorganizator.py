import os
import shutil, zipfile

columns = shutil.get_terminal_size().columns
print("---------------------------------".center(columns))
print("|primeiro coloque  onde vc deixa salvar os seus arquivos|".center(columns))
dest = input("  Entre com o destino dos arquivos: ")

print("|Escolha Algumas das opçoes      |".center(columns))
print("| arquivo de texto (.txt) = 1    |".center(columns))
print("| arquivo Excel    (.xlsx) = 2   |".center(columns))
print("----------------------------".center(columns))
Switch = int(input("Entre com a sua escolha: ".center(columns)))


# dest=destination of the file
#dest='C:/Users/souza/Documents/'


#src=os.chdir(srcinp)
if Switch==1:
    print("Entre com o caminho do arquivo de texto")
    src=input();
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)and full_file_name.endswith(".txt")):
            print("iniciando copia")
            shutil.copy(full_file_name, dest)
            print("copiado com sucesso")
            print("ok")
            
elif Switch==2:
    print("Entre com  o caminho do arquivo Excel(.xlsx)")
    src=input();
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)and full_file_name.endswith(".xlsx")):
            print("iniciando copia")
            shutil.copy(full_file_name, dest)
            print("copiado com sucesso")
            print("ok")
            


else:
    print("fail")

