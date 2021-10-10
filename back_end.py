import math

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians



def celsius_to_fahrenheit(celsius):
    '''
    Purpose: Converts celcius to farenheit
    Parameter(s): Celcius: The given temperture in celcius measurement
    Return Value: The temperature in farheneit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr


def circumference_circle(radius):
    """
    Purpose: Find the circumfrence of a circle
    Parameter(s): Radius of the given circle
    Return value: The cirles circumfrence
    """
    circum = (2 * math.pi * radius)
    return circum

def miles_to_kilometers(miles):
    """
    Purpose: Convert miles to kilometers
    Parameter(s): Distance in miles
    Return value: The distance in miles converted to kilometers
    """
    km = (miles * 1.609344)
    return km
def minutes_to_days(minutes):
    """
    Purpose: Convert minutes to minutes to days
    Parameter(s): The amount of time in minutes
    Return value: The amount of time in days
    """
    days = (minutes / 1440)
    return days


def trajectory(speed, height, angle):

    """Purpose: Find trajectory
    Parameters(s):
    Parmam1: The balls intital speed
    Paramm2: The balls intial height
    Parmam3: The Angle the ball is thrown relative to the ground
    Return value: the distance the ball traveled """
    radians = degrees_to_radians(angle)
    intialhs = (speed * (math.cos(radians)))
    intialvs = (speed * (math.sin(radians)))
    trajectory = (intialvs + math.sqrt((intialvs**2)+(19.6*height)))/9.8
    print(trajectory)
    distancetraveled = (intialhs * trajectory)
    print("Horizontal Speed: ", intialhs)
    print("Vertail Speed: ", intialvs)
    print("Flight Time: ", trajectory)
    return distancetraveled
