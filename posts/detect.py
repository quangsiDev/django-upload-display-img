import YOLO_func as yl
import cv2
    
    
image = cv2.imread("input1.jpg")
cv2.imwrite("object-detection.jpg", yl.detection(image))
