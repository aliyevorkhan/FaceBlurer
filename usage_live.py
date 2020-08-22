import cv2
import face_blurer

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640, 480)

    frame = face_blurer.blur_face(frame, 3)
    num_of_faces_frame = face_blurer.num_of_faces(frame)

    frame = cv2.putText(frame, str(num_of_faces_frame), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 3)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
