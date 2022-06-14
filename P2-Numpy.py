import cv2
import numpy as np
from random import randint

# img = cv2.imread("Artist.jpg")

# print(img)

#從直接讀取可以看到 圖片對於程式來說是由陣列組成
# print(type(img)) #多維陣列

# print(img.shape) #300 300 3
#意思是
#三個色順序並非RGB而是BGR
# [
#     [[1,2,3("三個值代表第三個，這邊分別代表BGR")],[1,2,3],[],[]..."300個代表第二個"],
#     [[1,2,3],[1,2,3],[],[]..."300個代表第二個"],
#     [[1,2,3],[1,2,3],[],[]..."300個代表第二個"],
#     [[1,2,3],[1,2,3],[],[]..."300個代表第二個"],
#     [[1,2,3],[1,2,3],[],[]..."300個代表第二個"],
#     ..."300個代表第一個"
# ]

#使用empty創造多維陣列 第一參數是長寬 以及每個單元的資料同上面介紹的
# img = np.empty((300,300,3),np.uint8)#0~255需要8bits,uint表正整數

# for row in range(300):
#     for column in range(300):
#         img[row][column]=[randint(0,255),randint(0,255),randint(0,255)]

# cv2.imshow("img",img)
# cv2.waitKey(0)


#
# img = cv2.imread("Artist.jpg")

# for row in range(50):
#     for column in range(img.shape[1]):#可以取寬度
#         img[row][column]=[randint(0,255),randint(0,255),randint(0,255)]

# cv2.imshow("img",img)
# cv2.waitKey(0)

#裁剪 第一個值為高度 第二個值為寬度
img = cv2.imread("Artist.jpg")

img=img[50:150,50:200]
cv2.imshow("img",img)
cv2.waitKey(0)