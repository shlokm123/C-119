import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)

def drawbox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(570,225,100),5)
    cv2.putText(img,"Tracking",(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(570,225,100),2)

while True:
    check,img = video.read()   
    succes,bbox = tracker.update(img)
    if succes:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"Lost",(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(570,225,100),2)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()


    