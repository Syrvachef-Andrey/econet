import cv2 as cv
import numpy as np

img = cv.imread('img/field-4.jpeg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=300,maxLineGap=10)
colors = np.linspace(0,255,len(lines))
i = 0
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(255,colors[i],0),2)
    i += 1
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()