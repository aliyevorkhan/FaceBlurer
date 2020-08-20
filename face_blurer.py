import cv2


def blur_face(image_path, level=1, show_image=True, save_image=False):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    # level_0 = 5  -> low 
    # level_1 = 11 -> mid 
    # level_2 = 17 -> high
    # and more
    bluring_level = (5+(level*6), 5+(level*6))
    
    if len(faces) != 0:         # If there are faces in the images
        for f in faces:         # For each face in the image
            # Get the origin co-ordinates and the length and width till where the face extends
            x, y, w, h = [v for v in f]
            sub_face = image[y:y+h, x:x+w]
            # apply a gaussian blur on this new recangle image
            sub_face = cv2.GaussianBlur(sub_face, bluring_level, 30)
            # merge this blurry rectangle to our final image
            image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

    if save_image:
        cv2.imwrite("result.jpg", image)

    if show_image:
        cv2.imshow("Result", image)
        cv2.waitKey(0)

def num_of_faces(image_path):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    return len(faces)
