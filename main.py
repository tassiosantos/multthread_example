from time import *
import numpy as np
import threading    

from logging import exception
from os import *
from datetime import date

from decimal import *





cinetic_energy_array = []
potential_energy_array = []
mass = 10
position0 = 0
velocity0 = 0
g = -10
tempo = []
    
def iniciar():

    print("Programa para calcular a energia cinética e potencial de uma particula lançada para cima")

def novo_cadastro():
    global potential_energy_array
    global cinetic_energy_array
    global mass 
    global position0
    global velocity0
    global g
    global tempo

    try:
        print("Digite a velocidade inicial:")
        velocity0 = int(input())
        
        print("Digite a gravidade:")
        g = int(input())
        
        print("Digite a massa do corpo:")
        mass = int(input())

        eventTime = abs(2*(velocity0/g))
        for i in np.linspace(0, eventTime, 10000):
                getcontext().prec = 3
                tempo.append(round(i, 1))
        
        #print(tempo)
    except:
        print("Erro no cadastro")

#Função para calcular a altura do corpo
def calculate_height (g, position0, velocity0, time): 
    height = position0 + (velocity0*time) + g*round((time**2),2)/2
    #print(height)
    return height
#Função para calcular a velocidade do corpo
def calculate_velocity (g, velocity0, time):
    velocity = velocity0 + (g*time)
    return velocity

#Função para calcular a energia cinética
def calculate_cinetic_energy(threadName, mass, g, velocity0, tempo):
    global cinetic_energy_array
    for t in tempo:
        velocity = calculate_velocity(g, velocity0, t)
        cinetic_energy = (mass*round((velocity**2),2))/2
        cinetic_energy_array.append(cinetic_energy)
        print(threadName, " : " ,cinetic_energy)

#Função para calcular a energia potencial
def calculate_potential_energy(threadName, mass, gravity, tempo):
    global potential_energy_array
    for t in tempo:
        height = calculate_height(g, 0, velocity0, t) 
        potential_energy = abs(mass*gravity*height)
        potential_energy_array.append(potential_energy)
        print(threadName, " : " ,potential_energy)


if __name__ == '__main__':
    
    iniciar()
    
    novo_cadastro()
    try:
        thread1 = threading.Thread(target = calculate_cinetic_energy, args=("Thread-1", mass, g, velocity0, tempo))
            
        thread2 = threading.Thread(target = calculate_potential_energy, args=("Thread-2", mass, g, tempo) )
        
        thread1.start()
        thread2.start()

    except:
        print("deu ruim")
