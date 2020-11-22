
from math import pi, asin, sin, sqrt, cos
def dist(latm,longm, lat, long):
    amer = latm*pi/180
    bmer = longm*pi/180
    ar = lat*pi/180
    br = long*pi/180
    R=6371
    d= R*2*asin(sqrt(((sin((ar-amer)/2))**2)+cos(amer)*cos(ar)*((sin((br-bmer)/2))**2)))
    return d
