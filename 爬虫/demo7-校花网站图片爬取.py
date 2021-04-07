# 导入爬虫库、html5lib、Beautifulsoup库
import requests
from bs4 import BeautifulSoup
import os
import urllib.request as req

# 1.请求url地址
url = 'http://www.gaokao.com/gkpic/'
response = requests.get(url)
# 测试状态：200 正常
# print(response)

# 创建本地文件夹
download = "xiaohua/"

# 当文件夹不存在时，创建新文件夹
if not os.path.exists(download):
    os.mkdir(download)


# 2.判断是否请求成功
if (response.status_code == 200):
    bs = BeautifulSoup(response.content, "html5lib")
    # 第二种方法：select select_one() 相当于 find() findall()
    # html css 选择器：id 类 标签
    divs = bs.find("div",attrs={"id": "imgall"})
    imgList = divs.find_all("img")

for i in range(len(imgList)):
    # 已经得到图片的网址
    src=imgList[i].get('src')
    # 把网址的类型转换成str型
    src2=str(src)
    # 下载
    # with open(download+src2.split("/")[-1], "wb") as file:
    #     file.write(requests.get(src2).content)
    # print(src2.split("/")[-1] + "下载成功")
    # 有点问题
    # req.urlretrieve(src)
    print("第{}张下载成功".format(i))













