import cv2

# read the image
actual_image = cv2.imread('flower_image.png')

# specifing image new size
desire_size = (500, 500)

# called resize function
resized_image = cv2.resize(actual_image, desire_size)

# add text upon actual_image
text = "Input Image"
position = (110, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (66, 235, 88)
thickness = 1
cv2.putText(actual_image, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

# showing the actual_image
cv2.imshow('Actual Images', actual_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# add text upon resized_image
text = "Output Image"
position = (150, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (66, 235, 88)
thickness = 1
cv2.putText(resized_image, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

# showing the resized_image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
