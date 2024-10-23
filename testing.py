import cv2

cap = cv2.VideoCapture('v4l2src ! video/x-raw, width=640, height=480 ! videoconvert ! appsink')
 # Try changing 0 to 1 or 2 if you have multiple cameras
if not cap.isOpened():
    print("Error: Could not open video source.")
else:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Test Camera", frame)
        cv2.waitKey(0)  # Press any key to close the window
    else:
        print("Error: Could not read frame from video source.")
cap.release()
cv2.destroyAllWindows()
