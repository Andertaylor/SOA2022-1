#emotion_detection.py
import cv2
from deepface import DeepFace

def emotion_detect():
    #Se cargan los nombres de las imagenes a partir del archivo generado por FileCounter.py
    f = open("../DataBase/input.txt","r")

    resultados = []

    #Se deben recorrer todas las imagenes en el archivo de input
    for fileName in f:
        size = len(fileName)
        #Lectura de la imagen segun el nombre leido en el input
        imagen = cv2.imread('../FacesDataBase/' + fileName[0:size-1])
        #Ejecucion del analisis de sentimientos
        analyze = DeepFace.analyze(imagen)  #here the first parameter is the image we want to analyze #the second one there is the action
        #Definicion de la emocion dominante
        emotion = analyze["dominant_emotion"]
        resultados.append(emotion)
    return response(resultados)

def response(resultados):
    
    #Genera un archivo con los nombres de las imagen
    f = open("../DataBase/output.txt", "w")
    for x in resultados:
        f.writelines(x + "\n")
    
emotion_detect()