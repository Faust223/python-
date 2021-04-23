# 导入库
import cv2

# 1.读取图片
# 2.彩色图片（三维）黑白图片（二维）

img = cv2.imread("pic/法蒂玛之手.png")

# print(img.shape) # () 高 宽 像素

# 2.显示图片
cv2.imshow("xxx.png")

# 显示图片默认会闪退
cv2.waitKey()



