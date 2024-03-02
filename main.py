import os
import cv2
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
while True:
    success, img = cap.read()
    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[3]
   # cv2.imshow("Webcam", img)
    cv2.imshow("face attendance", imgBackground)
    cv2.waitKey(1)