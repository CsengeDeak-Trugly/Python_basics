import qrcode

img = qrcode.make("https://www.instagram.com/trugly.photo/")
img.save("trugly_photo.jpg")

img = qrcode.make("The python is so funy, I love it! ")
img.save("python.jpg")

import cv2
d = cv2.QRCodeDetector()
retval, points, straight_qrcode= d.detectAndDecode(cv2.imread("python.jpg"))
print(retval)