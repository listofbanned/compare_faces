'''
by default: python compare_faces.py 
'''

import sys
import os
import cv2
import face_recognition
from drawer import Drawer
from detect_face import Detect

# 'src': the face you want to compare, 'src2compare': known face
try:
	# python compare_faces.py [image_you_want_to_compare.extension] [image_to_compare.extension]
	src = sys.argv[1]
	src2compare = sys.argv[2]
except:
	# by default
	src = './img.jpg'
	src2compare = './img2compare.jpg'

# load images with face_recognition
face = face_recognition.load_image_file(src)
face2compare = face_recognition.load_image_file(src2compare)

# change the default BGR channel to RGB
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
face2compare = cv2.cvtColor(face2compare, cv2.COLOR_BGR2RGB)

# load images with opencv, no need to change the color channel
#face = cv2.imread(src)
#face2compare = cv2.imread(src2compare)

# get the encoding of the faces
encoding_face = face_recognition.face_encodings(face)[0]
encoding_face2compare = face_recognition.face_encodings(face2compare)[0]

# compare faces
result = face_recognition.compare_faces([encoding_face], encoding_face2compare)
#print(result)
if True in result:
	Detect(face, os.path.basename(os.path.splitext(src)[0]))
else:
	print('No matches in detected faces.')
	Detect(face, 'unknown')
