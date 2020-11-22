
from math import pi, asin, sin, sqrt, cos
def dist(ame,bme, a, b):
    amer = ame*pi/180
    bmer = bme*pi/180
    ar = a*pi/180
    br = b*pi/180
    R=6371
    d= R*2*asin(sqrt(((sin((ar-amer)/2))**2)+cos(amer)*cos(ar)*((sin((br-bmer)/2))**2)))
    return d
