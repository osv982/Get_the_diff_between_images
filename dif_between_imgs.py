import cv2
from numpy import asarray


def compare_images():
    """сравнивает изображения и выдает разницу в процентах"""
    img_1 = "test_1_1.jpg"
    img_2 = "test_1_2.jpg"
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

    threshold = float(input('Введите пороговое значение на отрезке [0;255]\n'))
    flag = False
    while not flag:
        if 0 <= threshold <= 255:
            flag = True
        else:
            threshold = float(input('Значение неверно. Пожалуйста, введите еще раз\n'))

    count_dif_pix = 0
    for i in range(len(arr_pix_1)):
        for j in range(len(arr_pix_1)):
            # т к пиксели хранятся в uint8 от 0 до 255, то при взятии разности возникает исключение, поэтому приведем к int
            if abs(int(arr_pix_1[i][j]) - int(arr_pix_2[i][j])) > threshold:
                count_dif_pix += 1

    per_dif = (count_dif_pix / amount_pix) * 100

    if per_dif == 0:
        print("Изображения одинаковые")
    else:
        print("Изображения различаются на %.2f" % per_dif, "%")
