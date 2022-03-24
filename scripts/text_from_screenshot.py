import imp
from PIL import Image
import pytesseract
import os

pathToImage = r"C:\Users\gabri\Desktop\bebo\img"

imageList = [f for f in os.listdir(pathToImage) if f.endswith('.png')]
imageList.sort()

for i in imageList:
    im = Image.open(os.path.join(pathToImage, i))

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    textOutputTesseract = pytesseract.image_to_string(im, lang='eng+por')

    print(textOutputTesseract)
