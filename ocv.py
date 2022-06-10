import cv2

# Convert to Grayscale
# либо так
img_gray = cv2.imread("image_1.jpg", 0)
# либо так
# img_gray=cv2.imread("image_1.jpg")
# img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)

# преобразование изображения в нужный размер
res_img = cv2.resize(img_gray, (500, 900), cv2.INTER_NEAREST)

# def resizing(new_width=None, new_height=None, interp=cv2.INTER_LINEAR):
h, w = img_gray.shape[:2]
new_width, new_height = 16

# if new_width is None and new_height is None:
# return img_gray

if new_width is None:
    ratio = new_height / h
    dimension = (int(w * ratio), new_height)

else:
    ratio = new_width / w
    dimension = (new_width, int(h * ratio))

res_img = cv2.resize(img, dimension, interpolation=interp)

# To display Image
window_name = 'Grayscale Conversion OpenCV'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name, res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
