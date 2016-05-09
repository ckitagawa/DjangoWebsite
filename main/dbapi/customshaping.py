import cv2

img = cv2.imread('comp.png')

img = cv2.blur(img, img, Size(3,3))


cv2.imshow('image', img)
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()