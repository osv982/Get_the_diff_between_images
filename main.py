from PIL import Image  # основной модуль
from PIL import ImageChops


def diff():
    try:
        image_one = Image.open("image_1.jpg")
        image_two = Image.open("image_2.jpg")
    except FileNotFoundError:
        print("Файл не найден")

    diff = ImageChops.difference(image_one, image_two)

    if diff.getbbox():
        print("images are different")
    else:
        print("images are the same")


if __name__ == '__main__':
    diff()
    # original.show()  показать изображение