import cv2

# #讀取圖片
# img = cv2.imread("Artist.jpg")

# #調整圖片大小 參1目標圖片 參2長寬 參3長比例 參4寬比例 
# img_resized=cv2.resize(img,(300,300),fx=0.5,fy=o.5)


# #顯示圖片 參1視窗標題 參2目標圖片
# cv2.imshow("DOG",img)


# #由於上者會顯示之後會立馬關閉 因此需要
# #等待多久
# cv2.waitKey(5000)



#讀取影片
vid=cv2.VideoCapture(0)#可輸入檔名 而輸入零可以開啟本機的鏡頭

while True:#讀取每一幀並顯示出來
    ret,frame = vid.read()#此函式回傳兩個值 1為取得下一張有無成功->bool 2是如果1成功取得到的圖片
    if ret:
        frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)#當然也能調整大小
        cv2.imshow('vid',frame)
    else:#取得下一幀失敗跳出
        break
    if cv2.waitKey(10) == ord("q"):#這裏為等待毫秒 可藉此控制影片速度
        break#偵測q pressed 跳出