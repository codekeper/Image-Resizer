import cv2
import numpy as np

# read the image
actual_image = cv2.imread('flower_image.png')

# specifying image new size
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

# add text upon resized_image
text = "Output Image"
position = (150, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (66, 235, 88)
thickness = 1
cv2.putText(resized_image, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

# setting width & height for canvas(Background):
total_width = actual_image.shape[1] + resized_image.shape[1]
total_height = max(actual_image.shape[0], resized_image.shape[0])

# create a black background:
create_canvas = np.zeros((total_height, total_width, 3), dtype=np.uint8)

# placing image on the left side of the canvas:
create_canvas[:actual_image.shape[0], :actual_image.shape[1]] = actual_image

# placing image on the right side of the canvas:
create_canvas[:resized_image.shape[0], actual_image.shape[1]:] = resized_image

# showing the final results:
cv2.imshow("concatenated_image", create_canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
