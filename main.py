from PIL import Image  # основной модуль
from PIL import ImageChops
import cv2


def diff():
    # открываем изображения
    try:
        image_one = Image.open("image_1.jpg")
        image_two = Image.open("image_2.jpg")
    except FileNotFoundError:
        print("Файл не найден")

    # конвертируем в серый
    img_gray_1 = cv2.imread("image_1.jpg", 0)  # если не сработает то вместо image_one two их явные имена
    img_gray_2 = cv2.imread("image_2.jpg", 0)

    resizing(img_gray_1, 16, 16)
    resizing(img_gray_2, 16, 16)




# конвертируем в нужный размер
def resizing(img, new_width=None, new_height=None, interp=cv2.INTER_LINEAR):
    h, w = img.shape[:2]

    if new_width is None and new_height is None:
        return img

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
    cv2.imshow(window_name,  res_img)  # вывожу только одно изображение
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # return res_img


if __name__ == '__main__':
    diff()
    # original.show()  показать изображение
