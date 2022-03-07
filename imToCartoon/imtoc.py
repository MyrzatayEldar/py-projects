# import cv2
# import numpy as np 
# from google.colab.patches import cv2_imshow #This will help in displaying the image as we continue to modify it
# from google.colab import files 

# img = cv2.imread("eldar1.jpeg")

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray,5)
# edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

# color = cv2.bilateralFilter(img,9,250,250)
# cartoon = cv2.bitwise_and(color,color,mask=edges)

# cv2.imshow("Image",img)
# cv2.imshow("edges",edges)
# cv2.imshow("cartoon",cartoon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
a="python"
for i in range(len(a)):
	a[i] = i
print(a)
