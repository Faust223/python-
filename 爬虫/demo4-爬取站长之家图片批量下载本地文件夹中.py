import re
import requests
import os
# 站长之家页码
'''
https://sc.chinaz.com/tupian/meinvtupian.html
https://sc.chinaz.com/tupian/meinvtupian_2.html
https://sc.chinaz.com/tupian/meinvtupian_3.html
'''

# 第一页
urlFirst = 'https://sc.chinaz.com/tupian/meinvtupian.html'

# 第n页
urlBack = 'https://sc.chinaz.com/tupian/meinvtupian_{}.html'

# 创建本地文件夹
download = "picture/"

# 当本地文件夹不存在时
if not os.path.exists(download):
    os.mkdir(download)
url=""

# 4.循环
for i in range(1, 30):
    if(i == 1):
        url=urlFirst
    else:
        url=urlBack.format(i)
    # 发送请求获取url地址内容
    response = requests.get(url)
    imgUrlList = re.findall(r'<img src2="(.*)" alt=".*">', response.content.decode())
    for img in imgUrlList:
        # 图片下载
        print(type(img))
        with open(download+img.split("/")[-1],"wb") as file:
            file.write(requests.get("http:"+img).content)
        print(img.split("/")[-1]+"下载成功")
    print("第{}页下载成功".format(i))


