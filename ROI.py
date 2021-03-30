import cv2

im = cv2.imread("image-3.png")

roi = cv2.selectROI(im)

print(roi)

im_cropped= im[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]

cv2.imshow("Cropped Image",im_cropped)
cv2.imwrite("ROI-3.png", im_cropped)
cv2.waitKey(0)

