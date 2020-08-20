import sys
import face_blurer

# Get user supplied values
imagePath = sys.argv[1]

#face bluring method
face_blurer.blur_face(imagePath)

#get num of faces
print("Number of faces {0} ".format(face_blurer.num_of_faces(imagePath)))