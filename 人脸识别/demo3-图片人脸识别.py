import cv2
# 1.读取图片
img = cv2.imread("./pic/identity-card.jpg")

# 2.导入人脸识别的数据包
face_detect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# 3.使用鉴别器取识别图像
faces = face_detect.detectMultiScale(img)
# 4.识别到人脸后，返回的是二维列表
# x,y,w,h：分别表示脸的横坐标和宽高
for x,y,w,h in faces:
    # 参数一：识别图像数据
    # 参数二：人脸左上角坐标
    # 参数三：人脸右下角坐标
    # 参数四：标记的颜色
    # 参数五：绘图图形的宽度
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2)
    # 5.显示人脸
    cv2.imshow('identity-card',img)
    cv2.waitKey()








