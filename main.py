from time import time
import numpy as np

from logging import exception
from os import *
from datetime import date


import _thread      
    
def iniciar():

    return "null"

    #print("Programa para calcular a energia cinética e potencial de uma particula lançada para cima")

def novo_cadastro():
    global potential_energy_array
    global mass 
    global position0
    global velocity0
    global g
    global tempo

    try:
        tempo = []
        print("Digite a velocidade inicial:")
        velocity0 = int(input())
        
        print("Digite a gravidade:")
        g = int(input())
        
        print("Digite a massa do corpo:")
        mass = int(input())

        eventTime = 2*(velocity0/g)
        for i in np.linspace(0, eventTime, 100):
                tempo.append(i)
        
        #print(tempo)
    except:
        print("Erro no cadastro")

#Função para calcular a altura do corpo
def calculate_height (g, position0, velocity0, time): 
    height = position0 + (velocity0*time) + ((g*(time*time))/2)
    return height
#Função para calcular a velocidade do corpo
def calculate_velocity (g, velocity0, time):
    velocity = velocity0 + (g*time)
    return velocity

#Função para calcular a energia cinética
def calculate_cinetic_energy(threadName, mass, g, velocity0, time):
    global cinetic_energy_array
    print(time)
    for t in time:
        velocity = calculate_velocity(g, velocity0, t)
        cinetic_energy = (mass*(velocity*velocity))/2
        cinetic_energy_array.append(cinetic_energy)
        print(cinetic_energy)

def calculate_potential_energy(threadName, mass, gravity, height, time):
    global potential_energy_array
    for t in time:
        potential_energy = mass*gravity*height
        potential_energy_array.append(potential_energy)

if __name__ == '__main__':
    global potential_energy_array
    global cinetic_energy_array
    global mass 
    global position0
    global velocity0
    global g
    global tempo
    iniciar()
    
    novo_cadastro()
    
    try:
        

        potential_energy_array = []
        cinetic_energy_array = []

        _thread.start_new_thread(calculate_cinetic_energy, ("Thread-1", mass, g, velocity0, tempo))
            
        #thread2 = _thread.start_new_thread(calculate_potential_energy, ("Thread-2", mass, g, calculate_height(g, 0, velocity0, tempo) ) )
        #thread1.start()
        #thread2.start()


        
        #potential_energy_array = thread2.join()
        print(cinetic_energy_array)
    except:
        print("deu ruim")
