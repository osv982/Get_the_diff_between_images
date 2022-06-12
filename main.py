from PIL import Image  # основной модуль
from PIL import ImageChops

from numpy import asarray

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

    # конвертация в grayscale чтобы уменьшить шумы которые возникают при конвертации .
    # в 16 на 16 поэтому снчала конвертируем в 16 потом в серый
    # (Если вы не добавляете предварительную обработку, изображения должны иметь одинаковые размеры
    img_gray_1 = cv2.imread(img_1, 0)
    img_gray_2 = cv2.imread(img_2, 0)

    dimension = (16, 16)
    amount_pixels = dimension[0] * dimension[1]
    print(f"размер изображения: {amount_pixels} пикселей")

    # преобразование изображения в нужный размер  (столбец, строка)   print(len(numpydata_2)) дает количетсво строк
    res_img_1 = cv2.resize(img_gray_1, dimension, cv2.INTER_NEAREST)
    res_img_2 = cv2.resize(img_gray_2, dimension, cv2.INTER_NEAREST)

    # считывание пикселей в массив
    numpydata_1 = asarray(res_img_1)
    numpydata_2 = asarray(res_img_2)
    print(numpydata_1, '\n')
    print(numpydata_2)

    threshold = int(input('введите пороговое значение [0;255]\n'))
    count_dif_pix = 0

    for i in range(len(numpydata_1)):
        for j in range(len(numpydata_1)):
            # т к пиксели хранятся в uint8 от 0 до 255, то возникает исключение, поэтому приведем к int
            if abs(int(numpydata_1[i][j]) - int(numpydata_2[i][j])) > threshold:
                count_dif_pix += 1
    print(f"количество различных пикселей {count_dif_pix}")
    print(f"размер изображения: {amount_pixels} пикселей")

    per_dif = (count_dif_pix / amount_pixels) * 100

    if round(per_dif) == 0:
        print("изображения одинаковые")
    else:
        print(f"изображения различаются на {round(per_dif)} % ")

    #
    # # To display Image
    # window_name = 'Grayscale Conversion OpenCV'
    # cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.imshow(window_name, res_img_1)  # вывожу только одно изображение
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    diff()
    # original.show()  показать изображение
