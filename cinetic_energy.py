from moviment import *

def calculate_cinetic_energy(threadName, mass, g, velocity0, time):
    cinetic_energy_array = []
    for t in time:
        velocity = calculate_velocity(g, velocity0, t)
        cinetic_energy = (mass*(velocity*velocity))/2
        cinetic_energy_array.append(cinetic_energy)
