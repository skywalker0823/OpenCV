import cv2
import numpy as np

kernel=np.ones((8,8),np.uint8)
kernel2=np.ones((10,10),np.uint8)


#介紹常用的功能
img = cv2.imread("Artist.jpg")


# print(img.shape)



#BGR轉成灰階 第一個是目標 第二個是轉換方式 有多種可多嘗試
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#模糊化 高斯模糊 第一是目標 第二是核大小，必須是奇數 第三是標準差 後兩者可掌控模糊強度
img3=cv2.GaussianBlur(img,(7,7),3)

#取得圖片邊緣 第二是最低門檻 第三是最高門檻 沒達到最低門檻 將過濾掉不當成邊緣，超過最高門檻 全部當成邊緣
img4=cv2.Canny(img,150,200)

#膨脹(將邊緣變粗)第二是核 須為二維陣列 第三是膨脹次數
img5=cv2.dilate(img,kernel,iterations=1)

#收縮(將邊緣變細) 第二是核
img6=cv2.erode(img,kernel2,iterations=1)


cv2.imshow("img",img6)
cv2.waitKey(0)
