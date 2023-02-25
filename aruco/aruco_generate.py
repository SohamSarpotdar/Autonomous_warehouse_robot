import numpy as np
import cv2 as cv

aruco_type = cv.aruco.DICT_5X5_1000
aruco_type_name = "DICT_5X5_1000"
id = 7

arucoDict = cv.aruco.Dictionary_get(aruco_type)

print("ArUco type '{}' with '{}' id ".format(aruco_type,id))
tag_size = 1000
tag = np.zeros((tag_size,tag_size,1),dtype="uint8")
cv.aruco.drawMarker(arucoDict,id,tag_size,tag,1)

top = int(0.1*tag.shape[0])
bottom = top
left = int(0.1*tag.shape[1])
right = left
tag_withborders = cv.copyMakeBorder(tag,top,bottom,left,right,cv.BORDER_CONSTANT,None,(255,255,255))

tag_name = "arucoMarkers/" + aruco_type_name + "_" + str(id) + ".png"
cv.imwrite(tag_name,tag_withborders)
cv.imshow("ArUco Marker",tag_withborders)
cv.waitKey(0)
cv.destroyAllWindows()