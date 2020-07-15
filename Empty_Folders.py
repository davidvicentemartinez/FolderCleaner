import os, shutil, stat

def empty_folder(ruta):
    for (dirpath, dirnames, filenames) in os.walk(ruta):
        print(dirpath)
        if len(os.listdir(path=dirpath)) == 0:
            os.chmod( dirpath, stat.S_IWRITE )
            shutil.rmtree(dirpath, ignore_errors=True)
        

ruta = "G:/Nueva Carpeta/Nueva carpeta"
empty_folder(ruta)