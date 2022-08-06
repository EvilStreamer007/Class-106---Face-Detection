import cv2

img = cv2.imread("/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-106/4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-106/haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray,1.1,5)#change last value, to give max number of faces
print(faces)
print("Number of faces present: ",len(faces))

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       crop = img[y:y+h,x:x+w]
       cv2.imwrite("/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-106/cropped.jpg",crop)

cv2.imshow('img',img)
cv2.waitKey(0)
