import os, getpass

#class para criar  o folder para salvar arquivos
class makeFolder(object):
    
    def path_folder(path11):
        path11=os.path.join(*["C:/Users/"+getpass.getuser()+"/Documents/save"])
        if os.path.exists(path11):
            print("true")
        else:
            os.makedirs(path11, exist_ok=True)
            print("created")
