import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("error: could not open webcam")
    exit()
while True:
    ret,fram=cap.read()

    if not ret:
        print("Error: failed to capture image")
        break
    gray=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for(x,y,w,h) in faces:
        cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,0),2)
    font=cv2.FONT_HERSHEY_PLAIN
    cv2.putText(fram,f"people count: {len(faces)}",(10,30),font,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow("Face tracking and counting",fram)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print(f"People counting: {len(faces)}")
        break

cap.release()
cv2.destroyAllWindows()