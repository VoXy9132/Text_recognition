#Для работы требуется установка tesseract https://github.com/UB-Mannheim/tesseract/wiki
#и установить модули PIL и pytesseract

from PIL import Image
import pytesseract

def image_cropped(image, coordinates=(0, 0, 100, 100)):
    img = Image.open(image)
    img.crop(coordinates).save(f'{image}_cropped.jpg')
    img.close()
    return f'{image}_cropped.jpg'


def image_recognition(image, coordinates):
    #Следующая строка нужна, чтобы обозначить местонахождение tesseract.exe
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #
    image_name = image_cropped(image, coordinates=coordinates)
    image_file = Image.open(image_name)
    text = pytesseract.image_to_string(image_name)
    image_file.close()
    return text

def write_text(file, text):
    txt = open(file, encoding='utf-8', mode='a')
    txt.write(f'{text}')
    txt.close()


text = image_recognition('image.jpg', coordinates=(251, 362, 388, 385))
write_text('Texts.txt', text)

