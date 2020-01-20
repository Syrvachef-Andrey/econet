import cv2 as cv
import numpy as np
from scipy.spatial.distance import euclidean as dist
import matplotlib.pyplot as plt

def findLines(filename):
    img = cv.imread(filename)
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize = 3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=200, maxLineGap=10)
    
    return img, lines

def getEquations(lines):
    eqA = []
    eqB = []
    for line in lines:
        x = line[0][0::2]
        y = line[0][1::2]
        k, b = np.polyfit(x, y, 1)
        if k < 0:
            eqA += [(k, b)]
        else:
            eqB += [(k, b)]
    return eqA, eqB

def filterEquations(eqQ):
    res = []
    for k0, b0 in eqQ:
        nearest = []
        for k1, b1 in eqQ:
            if abs(k0-k1) < 1 and abs(b0-b1) < 15:
                nearest += [(k1, b1)]
        k, b = nearest[0]
        res += [(k, b)]
    return res

def extrapolate2(eqQ):
    K = [ k for k, b in eqQ]
    B = [ b for k, b in eqQ]
    
    X = list(range(len(K)))
    
    a, b, c = np.polyfit(X, sorted(K), 2)
    K1 = [ a*x**2 + b*x +c for x in range(-2, len(X)) ]
    a, b, c = np.polyfit(X, sorted(B), 2)
    B1 = [ a*x**2 + b*x +c for x in X ]

    return list(zip(K1, B1))
    
def extrapolate1(eqQ):
    sortedEq = sorted(eqQ, key=lambda x: x[0])
    plt.plot(range(len(eqQ)), [ x[1] for x in sortedEq ])
    plt.show()
    raise Exception
    K = [ k for k, b in eqQ]
    B = [ b for k, b in eqQ]

    X = list(range(len(K)))

    plt.plot(X, sorted(K))

    b, c = np.polyfit(X, sorted(K), 1)
    K1 = [ b*x +c for x in range(-2, len(X)) ]
    b, c = np.polyfit(X, sorted(B), 1)
    B1 = [ b*x +c for x in X ]
    
    plt.plot(X, K1)
    plt.show()
    return list(zip(K1, B1))

def solve(eqA, eqB):
    points = []
    for eqa in eqA:
        for eqb in eqB:
            a = [[1, -eqa[0]],[1, -eqb[0]]]
            b = [eqa[1],eqb[1]]
            x, y =  np.linalg.solve(a, b) 
            points += [(x,y)]
    filtered_points = []
    for a in points:
        nearest = []
        for b in points:
            if dist(a,b) < 20:
                nearest += [b]
        x, y = [ int(_) for _ in np.mean(nearest, axis=0) ]
        filtered_points += [(x, y)]
    return filtered_points

if __name__ == '__main__':
    img, lines = findLines('img/field-2.jpeg')
    eqA, eqB = [ filterEquations(eq) for eq in getEquations(lines) ]
    eqA = extrapolate1(eqA)
#    eqB = extrapolate1(eqB)
    #raise Exception
    points = solve(eqA, eqB)
    for eq in eqA + eqB:
        k, b = eq
        y0 = int(k *   0 + b)
        y1 = int(k * 640 + b)
        cv.line(img, (0, y0), (640, y1), (0,255,0), 1)
    for x, y in points:
        cv.circle(img, (int(y), int(x)), 5, (0,255,0), -1)    
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
#points = []
#for eqa in eqA:
#    for eqb in eqB:
#        a = [[1, -eqa[0]],[1, -eqb[0]]]
#        b = [eqa[1],eqb[1]]
#        x, y =  np.linalg.solve(a, b) 
#        points += [(x,y)]
##        cv.circle(img, (y, x), 2, (0,255,0), -1)
#
#    
    
    
