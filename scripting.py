import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#Define constants
grav = 6.67384 * (10 ** -11) # gravitational constant
  
m2 = 1.9891 * (10 ** 30) # mass of the sun

# Obtain values of the mass of the planet, its distance to the sun, wanted timescale,
# and its maximum velocity using a python dictionary, and asking for user input.
def getPlanetInfo(planet=None):
    """
    Defines the known masses, minimum distances to the Sun, and maximum 
    velocities for the planets of our solar system, as obtained from NASA data.
    Adapts the timescale on which the measurements are made later on,
    so that each graph shows about four full periods.
    """
    planetInfo = {
        'mercury': {'mass': 3.285e23, 'perihelion': 4.6e10, 'timescale':
3*10e6, 'velocity at perihelion':5.897e4, 'orbital period (in years)': 0.241, 'semi-major axis (in AU)': 0.39},
        'venus': {'mass': 4.867e24, 'perihelion': 1.0748e11, 'timescale':
7*10e6, 'velocity at perihelion':3.526e4, 'orbital period (in years)': 0.616, 'semi-major axis (in AU)': 0.72},
        'earth': {'mass': 5.972e24, 'perihelion': 1.47095e11, 'timescale':
1*10e7, 'velocity at perihelion':3.029e4, 'orbital period (in years)': 1, 'semi-major axis (in AU)': 1},
        'mars': {'mass': 6.39e23, 'perihelion': 2.0665e11, 'timescale':
2*10e7, 'velocity at perihelion': 2.65e4, 'orbital period (in years)': 1.882, 'semi-major axis (in AU)': 1.52},
        'jupiter': {'mass': 1.898e27, 'perihelion': 7.40595e11, 'timescale':
2*10e8, 'velocity at perihelion': 1.372e4, 'orbital period (in years)': 11.87, 'semi-major axis (in AU)': 5.2},
        'saturn': {'mass': 5.683e26, 'perihelion': 1.357554e12, 'timescale':
4*10e8, 'velocity at perihelion': 1.014e4, 'orbital period (in years)': 29.467, 'semi-major axis (in AU)': 9.58},
        'uranus': {'mass': 8.681e25, 'perihelion': 2.732696e12, 'timescale':
8*10e8, 'velocity at perihelion': 7.13e3, 'orbital period (in years)': 84.069, 'semi-major axis (in AU)': 19.2},
        'neptune': {'mass': 1.024e26, 'perihelion': 4.47105e12, 'timescale':
2*10e9, 'velocity at perihelion': 5.47e3, 'orbital period (in years)': 164.901, 'semi-major axis (in AU)': 30.05},
        'pluto' : {'mass': 0.013e24, 'perihelion': 4.4368e12, 'timescale':
7*10e9, 'velocity at perihelion': 6.1e3, 'orbital period (in years)': 248.109, 'semi-major axis (in AU)': 39.48},
        'zosia' : {'mass': 0.12e3, 'perihelion': 4.12 , 'timescale':
12*10e9, 'velocity at perihelion': 6.e1, 'orbital period (in years)': 19, 'semi-major axis (in AU)': 163}
    }

# Retrieve the information for the given planet
    if planet is None:
        return planetInfo
    planet = planet.lower()
    return planetInfo.get(planet, None)
    
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
    # planet is not available
else:
    print("Sorry, the information for", userPlanet, " is not available.")

# Defining initial values.
# planets start on the x-axis where y0=0.
# x0 is equal to the initial distance of the planet to the sun: 'x0', that has been chosen to be the perihelion above.
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
    rv : vector, x-position (x), y-position (y), x-velocity (vx) andy-velocity (vy)
    t : time
    Returns vector in the form of a tuple of four numbers (vx, vy, fx,fy)
-------
    Takes a vector containing x-position (x), y-position (y), x-velocity (vx) and y-velocity (vy)
    and a time parameter to calculate the right hand side of the ODE for a two body system
    and returns a tuple of four numbers,
    determining the forces acting on the system based on the position and the masses of the objects.
    """
    x, y, vx, vy = rv
    r = np.sqrt(x*x + y*y)
    fx = -grav*(m1 + m2)*(x/(r*r*r))
    fy = -grav*(m1 + m2)*(y/(r*r*r))
    return (vx, vy, fx, fy)

# assign every column of the array to its meaning
sol = integrate.odeint(rhs, init, t)
xpos = sol[:, 0]
ypos = sol[:, 1]
xvel = sol[:, 2]
yvel = sol[:, 3]

if planetInfo is not None:
    print("So the experimental perihelion is also %4.3E meters." %
np.max(xpos) )
    print('The experimental aphelion is %4.3E meters.' % np.abs(np.min(xpos)))

# graph of x and y positions over time
plt.plot(t , xpos, label = "x-position")
plt.plot(t , ypos, label = "y-position")
plt.title("Planet's position as projected on x- and y-axis")
plt.legend(loc ='best')
plt.xlabel('Time $(seconds)$')
plt.ylabel('Position relative to sun $(meters)$')
plt.grid()
plt.show()

# graph of x and y velocities over time
# for an ellips, the orbital velocity is higher when the planet is closer to the sun
plt.plot(t , xvel, color='pink', label="x-velocity")
plt.plot(t , yvel, color='purple', label="y-velocity")
plt.title("Planet's velocities in x- and y-direction")
plt.legend(loc='best')
plt.xlabel('Time $(seconds)$')
plt.ylabel('Velocities $(meters/second)$')
plt.grid()
plt.show()

# graph of x and y positions respective to each other, shows shape of orbit
plt.plot(xpos, ypos)
plt.title("Representation of planet's orbit")
plt.gca().set_aspect('equal')
plt.scatter(0, 0, color='pink', label='Sun')
plt.xlabel('Position $(meters)$')
plt.ylabel('Position $(meters)$')
plt.legend(loc='upper right')
plt.show()

### Checking Kepler --> 
"""
Square of the period "P" is proportional to the cube of the semimajor axis "a"
"""

allPlanets = getPlanetInfo()
for planet, info in allPlanets.items():
    P = info['orbital period (in years)']
    a = info['semi-major axis (in AU)']
#    print(f"{planet.capitalize()}: P = {P} years, a = {a} AU")

# Get all planet data
allPlanets = getPlanetInfo()

# Prepare lists for a and P
a_vals = []
P_vals = []
labels = []

for planet, info in allPlanets.items():
    P = info['orbital period (in years)']
    a = info['semi-major axis (in AU)']
    a_vals.append(a)
    P_vals.append(P)
    labels.append(planet.capitalize())

# Convert to numpy arrays
a_vals = np.array(a_vals)
P_vals = np.array(P_vals)

# Plotting on log-log scale
plt.loglog(a_vals, P_vals, 'o', label='Planetary Data')

# Label each point
for i, label in enumerate(labels):
    plt.text(a_vals[i], P_vals[i], label)

# Kepler's Law reference line: P = a^(3/2)
a_line = np.linspace(min(a_vals)*0.8, max(a_vals)*1.2, 100)
P_line = a_line ** (3/2)
plt.loglog(a_line, P_line, '--', label=r"Kepler's Law: $P \propto a^{3/2}$")

# Labels and grid
plt.xlabel("Semi-major axis $a$ (AU)")
plt.ylabel("Orbital period $P$ (years)")
plt.title("Kepler’s Third Law on Logarithmic Scale")
#plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
