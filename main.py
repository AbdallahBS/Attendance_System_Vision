import os
import pickle

import cv2
import face_recognition
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
#items display server
imgBackground = cv2.imread('Resources/background.png')
folderModePath = 'Resources/Modes'
modPathList = os.listdir(folderModePath)
imgModeList = []
for path in modPathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# import encoding file
print("Loading encoded file ....")
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
encodeListKnown , studentsIds = encodeListKnownWithIds
print(studentsIds)
print("encode file loaded")
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[3]

    for encodeFace , faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("matches " , matches )
        print("facedist", faceDis)
        matchIndex = np.argmin(faceDis)
      #  print(matchIndex)
        if(matchIndex ==0):
            print(" Hetha esmo abdallah !!!")


    print('Hetha mn3rfouch')
   # cv2.imshow("Webcam", img)
    cv2.imshow("face attendance", img)
    cv2.waitKey(1)