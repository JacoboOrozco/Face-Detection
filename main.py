import cv2

#Load opencv pre-trained data on face frontals (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
img = cv2.imread('RDJ.png')

#Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#To detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangles around the faces
cv2.rectangle(img, (220, 143), (220+219, 143+219), (0, 255, 0), 2)

print(face_coordinates)

#To show img
cv2.imshow('Clever Programmer Face Detector', img)

#In order to pause the execution of the code to be able to se img
cv2.waitKey()

print("Code Completed")