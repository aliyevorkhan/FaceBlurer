import sys
import face_blurer
import cv2

# Get user supplied values
image_path = sys.argv[1]

image = cv2.imread(image_path)

# face bluring method
image = face_blurer.blur_face(image)

cv2.imwrite("result.jpg", image)

cv2.imshow("Result", image)
cv2.waitKey(0)

# get num of faces
print("Number of faces {0} ".format(face_blurer.num_of_faces(image)))