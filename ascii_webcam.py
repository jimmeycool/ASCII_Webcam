import numpy as np
import cv2
import sys
import os

cap = cv2.VideoCapture(0)

asciiScale =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
width = 270
height = 90

# print row by row the ascii array
def printAscii(arr):
    sys.stdout.flush()
    for row in arr:
        for elem in row:
            sys.stdout.write(asciiScale[len(asciiScale) - elem -1])
        sys.stdout.write("\n")
    sys.stdout.write("\n")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    bigGrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(bigGrey,(width, height))

    # init ASCII array with normalized grey img
    asciiArr = np.zeros((width, height))
    asciiArr = cv2.normalize(gray,  asciiArr, 0, len(asciiScale)-1, cv2.NORM_MINMAX)

    # clear terminal and print ascii img (only linix systems atm)
    os.system("clear")
    printAscii(asciiArr)


    # Display the resulting frame
    # cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()