from distutils.fancy_getopt import fancy_getopt
import cv2

video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-106/haarcascade_frontalface_default.xml')

while(True):
    ret, frame = video.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grey,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow('Webcam',frame)

    if cv2.waitKey(25) == 32:
        break

video.release()
cv2.destroyAllWindows()
