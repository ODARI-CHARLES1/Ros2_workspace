import cv2
from ultralytics import YOLO # type: ignore
model=YOLO("yolo11n.pt")
camera=cv2.VideoCapture(0)

while True:
    ret,frame=camera.read()
    if not ret:
        break
    results=model(frame)
    output=results[0].plot()

    cv2.imshow("Robot Vision",output)

    if cv2.waitKey(1)==27:
        break

camera.release()
cv2.destroyAllWindows()