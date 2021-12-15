#código para definir as funções de movimento

def calculate_height (g, position0, velocity0, time): 
    height = position0 + (velocity0*time) + ((g*(time*time))/2)
    return height

def calculate_velocity (g, velocity0, time):
    velocity = velocity0 + (g*time)
    return velocity


