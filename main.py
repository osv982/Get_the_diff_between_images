from PIL import Image  # основной модуль
from PIL import ImageChops
import cv2


def diff():

    img_1 = "image_1.jpg"
    img_2 = "image_2.jpg"
    # открываем изображения
    try:
        image_one = cv2.imread(img_1)
        image_two = cv2.imread(img_2)
    except FileNotFoundError:
        print("Файл не найден")

    # конвертация в grayscale
    img_gray_1 = cv2.imread(img_1, 0)
    img_gray_2 = cv2.imread(img_2, 0)

    # преобразование изображения в нужный размер
    res_img_1 = cv2.resize(img_gray_1, (16, 16), cv2.INTER_NEAREST)
    res_img_2 = cv2.resize(img_gray_2, (16, 16), cv2.INTER_NEAREST)

    # To display Image
    window_name = 'Grayscale Conversion OpenCV'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, res_img_1)  # вывожу только одно изображение
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    diff()
    # original.show()  показать изображение
