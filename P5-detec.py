import cv2
import time

def emp(v):
    pass


#偵測顏色
img = cv2.imread("Artist.jpg")

img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#何為HSV? 相較於BGR更能夠去過濾顏色
#類似RGB的顏色表達方式 但是是依照 Hue色調 Saturation飽和度 Value亮度

#接著我們要找出"目標顏色的HSV"
#創立視窗並且指名長寬
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar',640,320)
#加入控制調 名稱 在哪 最小值 最大值 控制調被改變要調用的函式
cv2.createTrackbar('Hue Min','TrackBar',0,179,emp)
cv2.createTrackbar('Hue Max','TrackBar',179,179,emp)
cv2.createTrackbar('Sat Min','TrackBar',0,255,emp)
cv2.createTrackbar('Sat Max','TrackBar',255,255,emp)
cv2.createTrackbar('Val Min','TrackBar',0,255,emp)
cv2.createTrackbar('Val Max','TrackBar',255,255,emp)

while True:
    #可取得控制調上的值 監控項目 視窗 
    h_min=cv2.getTrackbarPos('Hue Min','TrackBar')
    h_max=cv2.getTrackbarPos('Hue Max','TrackBar')
    s_min=cv2.getTrackbarPos('Sat Min','TrackBar')
    s_max=cv2.getTrackbarPos('Sat max','TrackBar')
    v_min=cv2.getTrackbarPos('Val Min','TrackBar')
    v_max=cv2.getTrackbarPos('Val Max','TrackBar')
    print(
        'h_min:',h_min,'h_max:',h_max,'s_min:',s_min,'s_max:',s_max,'v_min:',v_min,'v_max:',v_max
    )
    #過濾 
    cv2.inRange(img,)

    cv2.waitKey()
cv2.imshow("img",img)
cv2.waitKey(0)
