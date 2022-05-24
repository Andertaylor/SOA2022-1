#jsonGenerator.py
import datetime
import json

def report_maker():
    #Se lee el archivo JSON existente y se carga como un diccionario
    with open("../DataBase/record.json") as json_file:
        data = json.load(json_file)

    #Definicion de los contadores
    countAngry = 0;    countDisgust = 0;     countFear = 0
    countHappy = 0;    countSad = 0;     countSurprise = 0
    countNeutral = 0

    #Se calcula la fecha actual
    date = datetime.datetime.now()
    thisMonth = "" + str(date.year) + "-" + str(date.month)

    #Se procede a revisar cada uno de los elementos, si cumple que es del mes actual procede a contar cuantas apariciones de cada sentimiento hay
    for element in data["Reportes"]:
        readedDate = element["fecha"]
        if thisMonth in readedDate:
            if (element["sentimiento"] == "angry"):
                countAngry+=1
            elif (element["sentimiento"] == "disgust"):
                countDisgust+=1
            elif (element["sentimiento"] == "fear"):
                countFear+=1
            elif (element["sentimiento"] == "happy"):
                countHappy+=1
            elif (element["sentimiento"] == "sad"):
                countSad+=1
            elif (element["sentimiento"] == "surprise"):
                countSurprise+=1
            elif (element["sentimiento"] == "neutral"):
                countNeutral+=1
            else:
                continue
        else:
            continue
                
    #Genera un archivo con los resultados
    lines = ["Para el mes " + str(date.month) + " del año " + str(date.year) + " se obtuvieron los siguientes resultados" + "\n", "Enojados: " + str(countAngry) + "\n", "Disgustado: " + str(countDisgust) + "\n", "Atemorizado: " + str(countFear) +"\n", "Felices: " + str(countHappy) + "\n", "Tristes: " + str(countSad) + "\n", "Sorprendidos: " + str(countSurprise) + "\n", "Indeferentes: " + str(countNeutral) + "\n"]
    with open("../DataBase/reporte.txt", "w") as f:
        f.writelines(lines)
 
report_maker()