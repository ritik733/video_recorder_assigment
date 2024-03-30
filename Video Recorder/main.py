import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

fourcc =  cv2.VideoWriter_fourcc('m','p','4','v')
writer = cv2.VideoWriter("recording.mp4", fourcc, 30.0 , (720,1280))

recording = True

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Video", frame)
        if recording:
            writer.write(frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('r'):
        recording = not recording
        print(f"Recording:{recording}")

cap.release()
writer.release()
cv2.destroyAllWindows()
