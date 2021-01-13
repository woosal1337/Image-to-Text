from PIL import Image, ImageGrab
from pathlib import Path
import time
import pytesseract as tess
import keyboard
from demo import queryMousePosition

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

totalEvent = 0
mouseCoordinatesDict = []

while True:
    try:

        if keyboard.is_pressed('q'):
            totalEvent += 1
            time.sleep(0.333)

            if totalEvent == 1:
                mouseCoordinates = queryMousePosition()
                print(mouseCoordinates)
                mouseCoordinatesDict.append(mouseCoordinates)
                pass

            if totalEvent == 2:
                mouseCoordinates = queryMousePosition()
                print(mouseCoordinates)
                time.sleep(0.333)
                mouseCoordinatesDict.append(mouseCoordinates)
                break

    except:
        break

print(mouseCoordinatesDict)

time.sleep(0.5)

image = ImageGrab.grab(bbox=(mouseCoordinatesDict[0][0], mouseCoordinatesDict[0][1], mouseCoordinatesDict[1][0],
                             mouseCoordinatesDict[1][1]))  # X1,Y1,X2,Y2
image.save("images/image.PNG")
openedImage = Image.open("images/image.PNG")

text = tess.image_to_string(openedImage)
print(text)
