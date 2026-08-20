Face Recognition is a computer vision technique used to identify or verify a person's identity by analyzing facial features. Unlike face detection, which only locates a face in an image, face recognition determines whether the detected face belongs to a known person.
In this project, the Face Recognition library is used to generate unique facial encodings for the known image and the test image. These facial encodings are then compared to determine whether both images belong to the same person. If the facial features match, the program displays "Matched"; otherwise, it displays "Unknown".
Face recognition is widely used in security, authentication, access-control, and identity verification applications.

Software Requirements
- Google Colab
- Python 3.x
- Face Recognition Library
- OpenCV
- Image containing a known face
- Image containing a test face

Procedure (Step-by-Step)

Step 1:
Open Google Colab.

Step 2:
Install the required libraries such as Face Recognition and OpenCV.

Step 3:
Import the required Python libraries.

Step 4:
Upload the known face image.

Step 5:
Upload the test face image.

Step 6:
Generate facial encodings for both images.

Step 7:
Compare the facial encodings to determine whether they belong to the same person.

Step 8:
Detect the face location in the test image.

Step 9:
Draw a bounding box around the detected face and display the result as Matched or Unknown.

Step 10:
Display the final output image.

Example

For (Matched)

Image 1 | Upload Known Face Image 
<img width="472" height="456" alt="image" src="https://github.com/user-attachments/assets/e2fcd8c9-4bcd-4e43-9139-b3b42f3f3ad9" />


Image 2 | Upload Test Face Image
<img width="472" height="456" alt="image" src="https://github.com/user-attachments/assets/7a5b4d1e-8d90-4eb7-ad85-3bcb6df4faa0" />

Recognised Face - Matched
<img width="472" height="456" alt="image" src="https://github.com/user-attachments/assets/b792a1f5-30e4-4155-86d0-e65695c161a8" />



For (Unknown)

Image 1 | Upload Known Face Image  
<img width="409" height="394" alt="image" src="https://github.com/user-attachments/assets/3b6ce268-afba-48e7-801a-dce90a4fcce4" />

Image 2 | Upload Test Face Image             
<img width="311" height="414" alt="image" src="https://github.com/user-attachments/assets/57d2e046-427c-4f67-8581-2fac3fcf2d69" />

Recognised Face- Unkonwn
<img width="377" height="503" alt="image" src="https://github.com/user-attachments/assets/ca43bb56-1d47-49c5-92fb-4e3f648b1e3e" />

Result

The Face Recognition system successfully compares the known and test face images and identifies whether the face is Matched or Unknown, while displaying the detected face with a bounding box.




