# 导入爬虫库、正则库
import requests
import re
import os
# 1.请求url地址
from pip._internal.commands import download

url = "https://sc.chinaz.com/tupian/210108513030.htm"

# 判断文件夹是否存在，不存在进行创建
if not os.path.exists(download):
    os.mkdir(download)

# 2.使用请求库向url请求，并接受请求
response = requests.get(url)

# 3.读取picture.html的所有内容，然后使用正则表达式提取图片路径
imgUrlList = re.findall(r'<img src="(.*)">', response.content.decode())
print(imgUrlList)

# 4.遍历列表
i = 1
for imgUrl in imgUrlList:
    with open("{}/{}.jpg".format(download,i), "wb") as file:
        file.write(requests.get("https:"+imgUrl).content)
    print("第{}张图片下载成功！".format(i))
    i += 1

#
