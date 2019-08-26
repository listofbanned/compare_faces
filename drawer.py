import os
import cv2
from datetime import datetime

def Drawer(img, landmarks, overlay_text, data):
	x1, x2, y1, y2 = data

	# landmarks
	landmarks_chin = []
	landmarks_left_eyebrow = []
	landmarks_right_eyebrow = []
	landmarks_nose_bridge = []
	landmarks_nose_tip = []
	landmarks_left_eye = []
	landmarks_right_eye = []
	landmarks_top_lip = []
	landmarks_bottom_lip = []

	# get detections to draw
	for landmark in landmarks:
		chin = landmark["chin"]
		left_eyebrow = landmark["left_eyebrow"]
		right_eyebrow = landmark["right_eyebrow"]
		nose_bridge = landmark["nose_bridge"]
		nose_tip = landmark["nose_tip"]
		left_eye = landmark["left_eye"]
		right_eye = landmark["right_eye"]
		top_lip = landmark["top_lip"]
		bottom_lip = landmark["bottom_lip"]

	# draw the face landmarks
	# chin
	for (a1, a2), (b1, b2) in zip(chin[:-1], chin[1:]):
		landmarks_chin.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_chin:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# left_eyebrow
	for (a1, a2), (b1, b2) in zip(left_eyebrow[:-1], left_eyebrow[1:]):
		landmarks_left_eyebrow.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_left_eyebrow:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# right_eyebrow
	for (a1, a2), (b1, b2) in zip(right_eyebrow[:-1], right_eyebrow[1:]):
		landmarks_right_eyebrow.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_right_eyebrow:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# nose_bridge
	for (a1, a2), (b1, b2) in zip(nose_bridge[:-1], nose_bridge[1:]):
		landmarks_nose_bridge.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_nose_bridge:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# nose_tip
	for (a1, a2), (b1, b2) in zip(nose_tip[:-1], nose_tip[1:]):
		landmarks_nose_tip.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_nose_tip:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# left_eye
	for (a1, a2), (b1, b2) in zip(left_eye[:-1], left_eye[1:]):
		landmarks_left_eye.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_left_eye:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# right_eye
	for (a1, a2), (b1, b2) in zip(right_eye[:-1], right_eye[1:]):
		landmarks_right_eye.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_right_eye:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# top_lip
	for (a1, a2), (b1, b2) in zip(top_lip[:-1], top_lip[1:]):
		landmarks_top_lip.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_top_lip:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# bottom_lip
	for (a1, a2), (b1, b2) in zip(bottom_lip[:-1], bottom_lip[1:]):
		landmarks_bottom_lip.append(((a1, a2), (b1, b2)))
	for c1, c2 in landmarks_bottom_lip:
		cv2.line(img, (c1[0], c1[1]), (c2[0], c2[1]), (0, 255, 0), 1)

	# assign/create folder to put the result
	output_path = './output/'
	if not os.path.exists(output_path):
		os.makedirs(output_path)

	# enclose detected face in a rect
	cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
	# put the name of the face (using the name of the image without extension)
	cv2.putText(img, overlay_text, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

	# file name
	file = output_path  + '%02s.png' % (str(datetime.now()))
	# write the file
	cv2.imwrite(file, img)
	# show result
	cv2.imshow('Detected face', img)
	cv2.waitKey(0)
