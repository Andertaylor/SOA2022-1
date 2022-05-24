#jsonGenerator.py
import datetime
import json

def json_generator():
    #Se calcula la fecha actual
    date = datetime.datetime.now()
    today = "" + str(date.year) + "-" + str(date.month) + "-" + str(date.day)

    #Se inicializan los arrays de valores
    fileNames = []
    emotions = []

    #Se cargan los resultados del analisis a partir del archivo generado por emotionDetect.py
    f1 = open("../DataBase/input.txt","r")

    for fileName in f1:
        sizeFileName = len(fileName)
        fileNames.append(fileName[0:sizeFileName-1])
    
    f2 = open("../DataBase/output.txt","r")

    for emotion in f2:
        sizeEmotion = len(emotion)
        emotions.append(emotion[0:sizeEmotion-1])

    #Se lee el archivo JSON existente y se carga como un diccionario
    with open("../DataBase/record.json") as json_file:
        data = json.load(json_file)

    sizeF1 = len(fileNames)
    sizeF2 = len(emotions)

    index = 0

    #Se deben recorrer todas las imagenes en el archivo de input
    while (index <  sizeF1) and (index < sizeF2):
        #Creacion de un nuevo diccionario para la nueva imagen
        newImageDict = {"fecha":today, "archivo": fileNames[index], "sentimiento": emotions[index]}
        data["Reportes"].append(newImageDict)
        index+=1

    #Se guarda el diccionario como archivo JSON
    with open("../DataBase/record.json", "w") as outfile:
        json.dump(data, outfile)
 
json_generator()