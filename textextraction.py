import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.pytesseract_cmd = 'C:\\Progam Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("D:/img/pancard2.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.medianBlur(img, 3)

img = img[210:440,0:680]

text = pytesseract.image_to_string(Image.open("D:/img/pancard2.png"))

print(text)

ret,bin = cv2.threshold(img, 182,255,cv2.THRESH_BINARY)
img = cv2.bitwise_not(bin)

cv2.imshow("image", img)
cv2.waitKeys(0)
