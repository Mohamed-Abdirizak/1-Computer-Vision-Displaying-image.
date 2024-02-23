import cv2

# 1: upload the image
img = cv2.imread('Annotation 2023-03-23 110010.png', 1)
# in sawirka aan yareeno, weeneenana. width, height
# imgWithResizeHW = cv2.resize(img, (500,400))

#resize the image using: x and y
# fx: 0.5 hadaan kadhigo geeska bidix ayuu image ka kudhagaa...
imgWithFxandFy = cv2.resize(img, (0,0), fx=1, fy = 1)

# rotate the image..
rotateImage = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# copying the image to new imge file..
cv2.imwrite('new_image.png', rotateImage)

# sawirkaani waa kii la rotate gareeye
cv2.imshow('Rotated Image', rotateImage)
# kana waa kii asalka ahaa.
cv2.imshow("Normal Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()