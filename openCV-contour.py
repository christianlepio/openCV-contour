import cv2 as cv
import numpy as np

img = cv.imread('img/bebe.jpg')

def resized(mat):
    width = int(mat.shape[1] * 0.6)
    height = int(mat.shape[0] * 0.6)
    dimension = width, height
    return cv.resize(mat, dimension, interpolation=cv.INTER_AREA)

imgResized = resized(img)
cv.imshow("me.photo", imgResized)

imgBlank = np.zeros((750, 700, 3) , dtype='uint8')
imgBlank[:] = 32, 0, 4

#CVT COLOR
imgGray = cv.cvtColor(imgResized, cv.COLOR_BGR2GRAY)
cv.imshow("me.grayScale", imgGray)

#CANNY
imgCanny = cv.Canny(imgGray, 100, 175)
cv.imshow("me.Canny", imgCanny)

#FIND CONTOURS
contour, hierarchy = cv.findContours(imgCanny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

#DRAW CONTOURS
cv.drawContours(imgBlank, contour, -1, (255,255,255), 1)

#RECTANGLE
cv.rectangle(imgBlank, (0, 410), (700, 750), (52, 11, 7), thickness=cv.FILLED)

#CIRCLE
cv.circle(imgBlank, (550, 160), 90, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (500, 120), 90, (32, 0, 4), thickness=cv.FILLED)
cv.circle(imgBlank, (490, 110), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (505, 300), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (650, 150), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (680, 300), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (60, 300), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (40, 40), 3, (255,255,255), thickness=cv.FILLED)
#start ng constellation
cv.circle(imgBlank, (300, 300), 3, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (345, 200), 4, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (390, 120), 4, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (450, 50), 4, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (470, 54), 3, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (499, 85), 3, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (465, 88), 3, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (435, 109), 3, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (600, 50), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (500, 30), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (650, 30), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (630, 290), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (400, 290), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (500, 250), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (450, 300), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (480, 180), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (500, 150), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (540, 120), 2, (255,255,255), thickness=cv.FILLED)
cv.circle(imgBlank, (540, 350), 2, (255,255,255), thickness=cv.FILLED)

#LINE
cv.line(imgBlank, (300, 300), (345, 200), (255, 255, 255), thickness=1)
cv.line(imgBlank, (345, 200), (390, 120), (255, 255, 255), thickness=1)
cv.line(imgBlank, (390, 120), (435, 109), (255, 255, 255), thickness=1)
cv.line(imgBlank, (435, 109), (450, 50), (255, 255, 255), thickness=1)
cv.line(imgBlank, (450, 50), (470, 54), (255, 255, 255), thickness=1)
cv.line(imgBlank, (470, 54), (465, 88), (255, 255, 255), thickness=1)
cv.line(imgBlank, (465, 88), (499, 85), (255, 255, 255), thickness=1)
cv.line(imgBlank, (499, 85), (490, 110), (255, 255, 255), thickness=1)
cv.line(imgBlank, (30, 450), (300, 450), (255, 255, 255), thickness=1)
cv.line(imgBlank, (340, 442), (605, 442), (255, 255, 255), thickness=1)
cv.line(imgBlank, (50, 500), (200, 500), (255, 255, 255), thickness=1)
cv.line(imgBlank, (190, 480), (290, 480), (255, 255, 255), thickness=1)
cv.line(imgBlank, (280, 490), (490, 490), (255, 255, 255), thickness=1)
cv.line(imgBlank, (480, 470), (690, 470), (255, 255, 255), thickness=1)
cv.line(imgBlank, (35, 530), (360, 530), (255, 255, 255), thickness=1)
cv.line(imgBlank, (373, 535), (695, 535), (255, 255, 255), thickness=1)
cv.line(imgBlank, (200, 560), (500, 560), (255, 255, 255), thickness=1)
cv.line(imgBlank, (490, 110), (435, 109), (255, 255, 255), thickness=1)

#RECTANGLE
cv.rectangle(imgBlank, (0, 600), (700, 750), (82, 24, 20), thickness=cv.FILLED)

#PUTTEXT
cv.putText(imgBlank, "Love Constellation", (5, 630), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.2, (255,255,255), thickness=1)
cv.putText(imgBlank, "(BSCS-4C)", (400, 630), cv.FONT_HERSHEY_DUPLEX, 1, (255,255,255), thickness=1)
cv.putText(imgBlank, "Carreon, Lepio, Tadena", (170, 680), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.2, (255,255,255), thickness=1)

cv.imshow("me.Contour", imgBlank)

bitwise_NOT = cv.bitwise_not(imgBlank)
cv.imshow('Bitwise NOT', bitwise_NOT)

cv.waitKey(0)