import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#Define constants
grav = 6.67 * (10 ** -11) # gravitational constant
  
m2 = 1.99 * (10 ** 30) #mass of the sun
# Obtain values of the mass of the planet, its distance to the sun, wanted timescale,
# and its maximum velocity using a python dictionary, and asking for user input.
def getPlanetInfo(planet):
    """
    Defines the known masses, minimum distances to the Sun, and maximum 
    velocities for the planets of our solar system, as obtained from NASA data.
    Adapts the timescale on which the measurements are made later on,
    so that each graph shows about four full periods.
    """
    planetInfo = {
        'mercury': {'mass': 3.285e23, 'perihelion': 4.6e10, 'timescale':
3*10e6, 'velocity at perihelion':5.897e4 },
        'venus': {'mass': 4.867e24, 'perihelion': 1.0748e11, 'timescale':
7*10e6, 'velocity at perihelion':3.526e4 },
        'earth': {'mass': 5.972e24, 'perihelion': 1.47095e11, 'timescale':
1*10e7, 'velocity at perihelion':3.029e4 },
        'mars': {'mass': 6.39e23, 'perihelion': 2.0665e11, 'timescale':
2*10e7, 'velocity at perihelion': 2.65e4 },
        'jupiter': {'mass': 1.898e27, 'perihelion': 7.40595e11, 'timescale':
2*10e8, 'velocity at perihelion': 1.372e4 },
        'saturn': {'mass': 5.683e26, 'perihelion': 1.357554e12, 'timescale':
4*10e8, 'velocity at perihelion': 1.014e4 },
        'uranus': {'mass': 8.681e25, 'perihelion': 2.732696e12, 'timescale':
8*10e8, 'velocity at perihelion': 7.13e3 },
        'neptune': {'mass': 1.024e26, 'perihelion': 4.47105e12, 'timescale':
2*10e9, 'velocity at perihelion': 5.47e3 },
       # 'pluto' : {'mass': 0.013e24, 'perihelion': 4.4368e12, 'timescale':
7*10e9, 'velocity at perihelion': 6.1e3 }


 # Convert the planet name to lowercase
    planet = planet.lower()
    # Retrieve the information for the given planet
    if planet in planetInfo:
        return planetInfo[planet]
    else:
        return None
# Ask the user to input a planet
userPlanet = input("Enter a planet: ")
# Get the information for the entered planet
planetInfo = getPlanetInfo(userPlanet)
# Check if the planet exists in the database
if planetInfo is not None:
    m1 = planetInfo['mass']
    x0 = planetInfo['perihelion']
    tScale = planetInfo[ 'timescale']
    vy0 = planetInfo[ 'velocity at perihelion']
    print("According to NASA data, the mass of", userPlanet," is", m1, "kilograms,")
    print("and the minimum distance from the Sun to", userPlanet," is %4.3E meters." % x0)
    # The code continues working with this planet mass and distance
    # Handle the case where the planet information is not available
else:
    print("Sorry, the information for", userPlanet, " is not available.")