
import cv2
body_classifier=cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Define a video capture object
cap = cv2.VideoCapture('walking.avi')

while(True):
   
    # Capture the video frame by frame
    ret, frame = cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body=body_classifier.detectMultiScale(grey,1.1,5)

    for (x,y,w,h) in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()


