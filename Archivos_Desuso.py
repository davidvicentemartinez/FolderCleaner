from datetime import datetime
import time
from pathlib import Path
import os, sys, stat
import shutil

tamaño_basura = 10 #En KB
tiempo_sin_uso = 365 #En días
ruta = "G:/Nueva carpeta/Nueva carpeta"
destino = "G:/Antiguo/"

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d')
    return formated_date

def manage_file(file):
    statinfo = os.stat(file)
    file_size = statinfo.st_size
    if (file.endswith(".nfo") or file.endswith(".txt") or file.endswith("RARBG_DO_NOT_MIRROR")) and (file_size <= (tamaño_basura * 1024)):
        os.remove(file)
    else:
        access_time = statinfo.st_atime
        dif_a_time = time.time() - access_time
        if dif_a_time >= (tiempo_sin_uso * 24 * 60 * 60):
            return True
    return False


def get_files(ruta):
    for (dirpath, dirnames, filenames) in os.walk(ruta):
        for file in filenames:
            file_f = os.path.join(dirpath,file)
            if manage_file(file_f):
                os.replace(file_f,destino + file)
        for file in dirnames:
            file_f = os.path.join(dirpath,file)
            if manage_file(file_f):
                os.replace(file_f,destino + file)


get_files(ruta)

