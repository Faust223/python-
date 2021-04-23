import cv2

# 1.读取图片
img = cv2.imread("./pic/xxx.png")

# 2.将图片转换为灰度图
# 参数一：读取原图数据
gray_hand = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3.显示
cv2.imshow("hand",gray_hand)

# 4.延迟时间

cv2.waitKey()



