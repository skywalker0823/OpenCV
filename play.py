import cv2


vid=cv2.VideoCapture(0)#可輸入檔名 而輸入零可以開啟本機的鏡頭

#多使用shape來取長寬

while True:#讀取每一幀並顯示出來
    ret,frame = vid.read()#此函式回傳兩個值 1為取得下一張有無成功->bool 2是如果1成功取得到的圖片
    if ret:
        frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)#當然也能調整大小
        # cv2.line(frame,(200,0),(200,600),(0,255,0),1)#線條

        # cv2.rectangle(frame,(150,150),(300,300),(0,255,0),1)

        # frame=cv2.Canny(frame,100,150)#邊緣



        color = (0, 255, 0)  # 定義框的顏色
    
        # OpenCV 人臉識別分類器
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
        # 調用偵測識別人臉函式
        faceRects = face_classifier.detectMultiScale(
            frame, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        
        # 大於 0 則檢測到人臉
        if len(faceRects):  
            # 框出每一張人臉
            for faceRect in faceRects: 
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x, y), (x + h, y + w), color, 2)
        





        cv2.imshow('vid',frame)
    else:#取得下一幀失敗跳出
        break
    if cv2.waitKey(10) == ord("q"):#這裏為等待毫秒 可藉此控制影片速度
        break#偵測q pressed 跳出