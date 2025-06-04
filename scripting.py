import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#Define constants
#exec(open("/Users/luciehoeberichts/Downloads/UCSCIMATL2_NotebooksForBrightspace 4/LuZo_orbiting/Zocie_orbits/scripting.py").read())

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
        'pluto' : {'mass': 0.013e24, 'perihelion': 4.4368e12, 'timescale':
7*10e9, 'velocity at perihelion': 6.1e3 }
    }

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

# Defining initial values.
# In this model, planets start on the x-axis where y0=0.
# x0 then is equal to the initial distance of the planet to the sun: 'x0',
# that has been chosen to be the perihelion above.
# Velocity in x-direction is temporarily 0 if planet is on the x-axis, so vx0 is put equal to 0.
# Velocity in y-direction is at its maximum value in the perihelium, asdefined above.
x0, y0, vx0, vy0 = x0, 0, 0, vy0
init= [x0,y0,vx0,vy0]
t = np.linspace(0, tScale, 400)
# define function that will return experimental values for velocities andpositions
def rhs(rv, t):
    """
    Parameters
    ----------
    rv : vector containing x-position (x), y-position (y), x-velocity (vx) andy-velocity (vy)
    t : time
    Returns another vector in the form of a tuple of four numbers (vx, vy, fx,fy)
-------
    Takes a vector containing x-position (x), y-position (y), x-velocity (vx) and y-velocity (vy)
    and a time parameter to calculate the right hand side of the ODE for a two body system
    and returns a tuple of four numbers. The calculation involves determining the forces
    acting on the system based on the position and the masses of the objects.
    """
    x, y, vx, vy = rv
    r = np.sqrt(x*x + y*y)
    fx = -grav*(m1 + m2)*(x/(r*r*r))
    fy = -grav*(m1 + m2)*(y/(r*r*r))
    return (vx, vy, fx, fy)
