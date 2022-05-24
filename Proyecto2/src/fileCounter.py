#emotion_detection.py
from time import sleep
import os

def file_count():
    count = 0
    while(count < 10):
        archivos = os.listdir("../FacesDataBase")
        print(archivos)
        print(len(archivos))
        count = len(archivos)
        sleep(2)
    return response(archivos)

def response(archivos):
    
    #Genera un archivo con los nombres de las imagen
    f = open("../DataBase/input.txt", "w")
    for x in archivos:
        f.writelines(x + "\n")
        
file_count()


