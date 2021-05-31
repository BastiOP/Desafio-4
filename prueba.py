import math
import random
import csv
random.seed(5)

class Neurona:
    def __init__(self, valor, delta, capaAnterior, capaSiguiente, pesosAnterior, auxPesos):
        self.valor = valor #Valor Flotante
        self.delta = delta #valor Flotante
        self.capaAnterior = capaAnterior #Lista de Neuronas
        self.capaSiguiente = capaSiguiente #Lista de Neuronas
        self.pesosAnterior = pesosAnterior #Lista de Flotantes
        self.auxPesos = auxPesos #Lista de Flotantes
    
    def print_neurona(self):
        print("Valor:", self.valor)
        print("Delta:",self.delta)
        print()

    def funcionActivacion(self): #Retorna Flotante
        return pow(( 1 + math.exp(self.valor)),-1)

    def derivadaFuncionActivacion(self): #Retorna Flotante
        return self.funcionActivacion()*(1-self.funcionActivacion())

    def calculaValor(self):
        total = 0.0
        for i in range(len(self.capaAnterior)):
            total += (self.capaAnterior[i]).funcionActivacion()*self.pesosAnterior[i]
        self.valor = total

    def calcularNuevoPeso(self, learningRate, valorEsperado):
        if self.capaSiguiente == None:
            self.delta = (self.funcionActivacion()-valorEsperado)*self.derivadaFuncionActivacion()
            for i in range(len(self.capaAnterior)):
                self.capaAnterior[i].delta += self.delta*self.pesosAnterior[i]
                self.auxPesos.append(self.pesosAnterior[i]-(learningRate*(self.capaAnterior[i].funcionActivacion()*self.delta)))
            self.delta = 0
        else:
            self.delta = self.delta*self.derivadaFuncionActivacion()
            for i in range(len(self.capaAnterior)):
                self.capaAnterior[i].delta += self.delta*self.pesosAnterior[i]
                self.auxPesos.append(self.pesosAnterior[i]-(learningRate*(self.capaAnterior[i].funcionActivacion()*self.delta)))
            self.delta = 0


class Red:
    def __init__(self, capas):
        self.capas = capas #Lista de Listas de Neuronas

    def print_capas(self):
        for i in R.capas:
            for j in i:
                print(j.valor, end=" ")
            print()

    def print_peso_capas(self):
        for i in R.capas:
            for j in i:
                print(j.pesosAnterior)
            print()

    def crearRedVacia(self, numNeuronasEntrada, numNeuronasSalida):
        self.agregarCapa(numNeuronasEntrada)
        self.agregarCapa(5)
        #self.agregarCapa(7)
        #self.agregarCapa(4)
        self.agregarCapa(numNeuronasSalida)

    def agregarCapa(self, numNeuronas):
        temp = [] #Lista de Neuronas
        for i in range(numNeuronas):
            temp.append(Neurona(0,0,None,None,None,[])) 
        if len(self.capas) == 0 :
            self.capas.append(temp)
        else:       
            for i in range(numNeuronas) :
                pesosTemp = [] #Lista de Flotantes
                for j in range(len(self.capas[len(self.capas)-1])) :
                    pesosTemp.append(random.uniform(-6.0, 6.0)) #Aleatoreo del -6 al 6
                temp[i].capaAnterior = self.capas[len(self.capas)-1]
                temp[i].pesosAnterior = pesosTemp
            for i in range(len(self.capas[-1])):
                self.capas[-1][i].capaSiguiente = temp
            self.capas.append(temp)
    
    def predict(self, input):
        salida = [] #Lista de Flotantes
        for i in range(len(self.capas[0])):
            self.capas[0][i].valor = input[i]

        for i in range(1, len(self.capas)):
            for j in range(len(self.capas[i])):
                self.capas[i][j].calculaValor()
        for i in range(len(self.capas[-1])):
            salida.append(self.capas[-1][i].funcionActivacion())
        return salida

    def actualizaPesos(self, learningRate, valorEsperado): #Equipo 1 sera el indice 0, Equipo 2 sera el indice 1
        for i in range(len(self.capas)-1, 0, -1):
            for j in range(len(self.capas[i])):
                if i == len(self.capas)-1:
                    self.capas[i][j].calcularNuevoPeso(learningRate,valorEsperado[j])
                else:
                    self.capas[i][j].calcularNuevoPeso(learningRate,valorEsperado[1])
        for i in range(1, len(self.capas)):
            for j in range(len(self.capas[i])):
                self.capas[i][j].pesosAnterior = self.capas[i][j].auxPesos[:]
                self.capas[i][j].auxPesos = []
                self.capas[i][j].calculaValor()
            
def entrenar(Red, instanciaEntrenamiento, valoresEsperados, numIteraciones, learningRate):
    listaRandom = random.sample(range(len(instanciaEntrenamiento)), k=numIteraciones)
    i = 0
    for instancia in listaRandom:
        valorPredecido = Red.predict(instanciaEntrenamiento[instancia])
        print("Iteracion", i+1, ":", valorPredecido, valoresEsperados[instancia])
        Red.actualizaPesos(learningRate, valoresEsperados[instancia])
        i += 1
    print("Cantidad de iteraciones:",numIteraciones," Learning Rate:", learningRate)

def probar(Red, instanciaPrueba, valoresEsperados, numIteraciones):
    listaRandom = random.sample(range(len(instanciaPrueba)), k=numIteraciones)
    bienPredecidos = 0
    i = 0
    for instancia in listaRandom:
        valorPredecido = Red.predict(instanciaPrueba[instancia])
        print("Iteracion", i+1, ":", valorPredecido, valoresEsperados[instancia])
        if (valorPredecido[0] > valorPredecido[1] and valoresEsperados[instancia][0] > valoresEsperados[instancia][1]) or (valorPredecido[0] < valorPredecido[1] and valoresEsperados[instancia][0] < valoresEsperados[instancia][1]):
            bienPredecidos += 1
        i += 1
    print("Cantidad de iteraciones:",numIteraciones)
    print("Precision:",(100*bienPredecidos)/numIteraciones,"%")

input = []
output = []

with open('games4.csv', newline='') as file: #se abre y se lee el archivo 
    file.readline()
    for line in file:  #linea por linea, se elimina el salto de linea y se separa por coma, para luego agregar a la lista de input
        line = line.replace('\r','')
        linea = line.split(';')
        for i in range(0, len(linea)): 
            linea[i] = int(linea[i])
        input.append(linea)

for i in range(len(input)): #es agregado al output los ganadores y eliminados del input
    if input[i][0] == 1:
        output.append([1, 0])
    else:
        output.append([0, 1])
    input[i].pop(0)

cantNeuronasEntrada = len(input[0])
cantNeuronasSalida = len(output[0])


inputEntrenamiento = input[:round(len(input)*0.7)]
inputPruebas = input[round(len(input)*0.7):]

R = Red([])
R.crearRedVacia(cantNeuronasEntrada, cantNeuronasSalida)

entrenar(R, inputEntrenamiento, output[:round(len(input)*0.7)], len(inputEntrenamiento), 0.1)
probar(R, inputPruebas, output[round(len(input)*0.7):], len(inputPruebas))

