import cv2

actual_image = cv2.imread('flower_image.png')

desire_size = (500, 500)

resized_image = cv2.resize(actual_image, desire_size)

text = "Input Image"
position = (110, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (66, 235, 88)
thickness = 1
cv2.putText(actual_image, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

cv2.imshow('Actual Images', actual_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = "Input Image"
position = (110, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (66, 235, 88)
thickness = 1
cv2.putText(actual_image, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
