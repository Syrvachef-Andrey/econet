import cv2 as cv
import numpy as np
from scipy.spatial.distance import euclidean as dist

img = cv.imread('img/field-1.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize = 3)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=200, maxLineGap=10)
colors = np.linspace(0,255,len(lines))
i = 0

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

points = []
for eqa in eqA:
    for eqb in eqB:
        a = [[1, -eqa[0]],[1, -eqb[0]]]
        b = [eqa[1],eqb[1]]
        x, y =  np.linalg.solve(a, b) 
        points += [(x,y)]
#        cv.circle(img, (y, x), 2, (0,255,0), -1)

p = []
for a in points:
    nearest = []
    for b in points:
        if dist(a,b) < 20:
            nearest += [b]
    x, y = [ int(_) for _ in np.mean(nearest, axis=0) ]
    cv.circle(img, (y, x), 2, (0,255,0), -1)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()