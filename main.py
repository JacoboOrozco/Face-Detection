import cv2

#Load opencv pre-trained data on face frontals (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
#img = cv2.imread('FRIENDS.png')

#To capture from video from webcam
webcam = cv2.VideoCapture(0)

#Iterate forever over webcam frames
while True:
    #Read current frame
    successful_frame_read, frame = webcam.read()

    #Must convert to grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #To detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    #Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Show frame
    cv2.imshow('Clever Programmer Face Detector', frame)

    key = cv2.waitKey(1)

    #Stop if Q key is pressed
    if key == 81 or key == 113:
        break

#Release the videocapture object
webcam.release()

print("Code Completed")

