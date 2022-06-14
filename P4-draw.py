import cv2
import numpy as np

#創造黑色畫布
#創造值為零的陣列
img=np.zeros((600,600,3),np.uint8)

#直線 設定起始和終點 和顏色 及寬度
# cv2.line(img,(1,1),(600,600),(255,255,255),1)

#方形 最後參數輸入filled可以填滿
# cv2.rectangle(img,(0,0),(100,150),(0,255,0),1)

#circle 中心點 半徑 顏色 寬度
cv2.circle(img,(150,150),30,(0,255,0),3)

#寫字 內容 座標 字體 大小 顏色 粗度
cv2.putText(img,"HELLO",(100,150),cv2.FONT_ITALIC,1,(0,255,0),1)

cv2.imshow("img",img)
cv2.waitKey(0)