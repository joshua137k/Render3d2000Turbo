import math
from numba import njit


w,h = 800,600
cx,cy = w//2,h//2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)


distance = lambda i,t: math.sqrt((i[0]-t[0])**2 + (i[1]-t[1])**2 +(i[2]-t[2])**2 )
minus = lambda k,t: [k[i]-t[i] for i in range(len(t))]


@njit
def rotate2d(pos,rad): 
	x,y=pos
	s,c = math.sin(rad),math.cos(rad)
	return (-y*s + x*c),( y*c + x*s)

@njit
def rotateX(point, rad):
    x, y, z = point
    return (x, y*math.cos(rad) - z*math.sin(rad), y*math.sin(rad) + z*math.cos(rad))

@njit
def rotateY(point, rad):
    x, y, z = point
    return (x*math.cos(rad) + z*math.sin(rad), y, -x*math.sin(rad) + z*math.cos(rad))

@njit
def rotateZ(point, rad):
    x, y, z = point
    return (x*math.cos(rad) - y*math.sin(rad), x*math.sin(rad) + y*math.cos(rad), z)


