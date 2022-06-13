import cv2
from numpy import asarray
from service import my_input


def compare_images():
    """сравнивает изображения и выдает разницу в процентах"""

    path = "./tests/test_1/test_1_input/"
    img_1 = path + "test_1_1.jpg"
    img_2 = path + "test_1_2.jpg"

    # открываем изображения
    try:
        image_one = cv2.imread(img_1)
        image_two = cv2.imread(img_2)
    except FileNotFoundError:
        print("Файл не найден")

    # конвертация в grayscale, чтобы вместо 3-х значений пикселя получить 1 и сравнивать только яркость пикселей, а не цвет
    img_gray_1 = cv2.imread(img_1, 0)
    img_gray_2 = cv2.imread(img_2, 0)

    dimension = (16, 16)
    amount_pix = dimension[0] * dimension[1]

    # преобразование изображений в одинаковый требуемый размер
    res_img_1 = cv2.resize(img_gray_1, dimension, cv2.INTER_AREA)
    res_img_2 = cv2.resize(img_gray_2, dimension, cv2.INTER_AREA)

    # чтение пикселей в массив
    arr_pix_1 = asarray(res_img_1)
    arr_pix_2 = asarray(res_img_2)

    threshold = my_input()

    count_dif_pix = 0
    for i in range(len(arr_pix_1)):
        for j in range(len(arr_pix_1)):
            if abs(int(arr_pix_1[i][j]) - int(arr_pix_2[i][j])) > threshold:
                count_dif_pix += 1

    per_dif = (count_dif_pix / amount_pix) * 100

    if per_dif == 0:
        print("Изображения одинаковые")
    else:
        print("Изображения различаются на %.2f" % per_dif, "%")
