# Install Library
!pip install face_recognition opencv-python-headless -q

# Import Libraries
import face_recognition
import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload Known Image
print("Upload Known Image")
uploaded = files.upload()
known_name = list(uploaded.keys())[0]

# Upload Test Image
print("Upload Test Image")
uploaded = files.upload()
test_name = list(uploaded.keys())[0]

# Load Images
known_image = face_recognition.load_image_file(known_name)
test_image = face_recognition.load_image_file(test_name)

# Encode Faces
known_encoding = face_recognition.face_encodings(known_image)[0]
test_encoding = face_recognition.face_encodings(test_image)[0]

# Calculate Face Distance
distance = face_recognition.face_distance([known_encoding], test_encoding)[0]
print("Face Distance:", distance)

# Match Decision
if distance < 0.40:
    label = "Matched"
else:
    label = "Unknown"

# Detect Face Location
face_locations = face_recognition.face_locations(test_image)

# Read Test Image
img = cv2.imread(test_name)

# Draw Box and Label
for (top, right, bottom, left) in face_locations:

    cv2.rectangle(img, (left, top), (right, bottom), (0,255,0), 2)

    cv2.putText(img, label,
                (left, top-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2)

# Show Output
cv2_imshow(img)
