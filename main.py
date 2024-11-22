from deepface import DeepFace
import os
os.environ["SSL_CERT_FILE"] = "cab.crt"

#match 2 images
# result = DeepFace.verify(img1_path = "img4.jpg",img2_path = "img6.jpg")
# print(result["verified"])

#find in db
# result = DeepFace.find(img_path="img5.jpg",db_path="db")
# print(result)

import threading
import cv2 
from deepface import DeepFace

cap = cv2.VideoCapture (0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

reference_img = cv2.imread("profile.png")

def check_face(frame):
  global face_match
  global face_check

  try:
    results = DeepFace.find(img_path=frame,db_path="db")
    
    if (len(results) == 1 and len(results[0]["identity"]._values) != 0):
      face_match=True
      face_check=results[0]["identity"][0]
    else:
      face_match=False
  except ValueError: 
    face_match=False
 
while True:

 ret, frame = cap.read()

 if ret:
    if counter % 38 == 8:

      try:
       threading. Thread(target=check_face, args=(frame.copy(),)).start() 
      except ValueError:

       pass
    counter += 1

    if face_match:

      cv2.putText(frame, face_check, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    else:

     cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("video", frame)
 key = cv2.waitKey(1)
 if key == ord("q"):
    break
cv2.destroyAllWindows()
