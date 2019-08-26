import cv2
import face_recognition
from drawer import Drawer

def Detect(img, overlay_text):
	# converting RGB image to grey scale
	grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	# locate face and face landmarks
	face = face_recognition.face_locations(grey_img)
	landmarks = face_recognition.face_landmarks(grey_img)

	# calculate (reorder) x1, x2, y1, y2
	for top, right, bottom, left in face:
		x1, x2, y1, y2 = left, right, top, bottom

	# draw the results
	Drawer(img, landmarks, overlay_text, (x1, x2, y1, y2))
