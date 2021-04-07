import os
import requests
from bs4 import BeautifulSoup


# 1.请求url地址

url = "http://www.xbiquge.la/2/1690/"
response = requests.get(url)

# 创建本地文件夹
download = "novel/"

# 当本地文件夹不存在时
if not os.path.exists(download):
    os.mkdir(download)



# 2.判断是否请求成功

if (response.status_code== 200):
    # 使用bs4和html5lib解析网页内容
    bs = BeautifulSoup(response.content,"html5lib")
    # print(bs)
    divs = bs.find("div", attrs={"id":"list"})
    # 再找a标签 findall():返回结果是多个
    aList = divs.find_all("a")
    # 循环遍历
    for a in aList:
        # 获取文本内容
        title = a.text
        # href地址
        hrefList = a.get("href")
        # 字符串拆分
        listText = hrefList.split("/")[-1]
        # 获取子路径
        urlList = url+listText
        # 发送请求
        resp = requests.get(urlList)
        if(resp.status_code == 200):
            # 使用bs4和html5lib解析
            b = BeautifulSoup(resp.content,"html5lib")
            childText = b.find("div",attrs={"id":"content"}).text
            # 写到本地文件夹中
            with open(download+title+".txt","w",encoding="utf-8") as file:
                file.write(childText)
            print(title+"下载成功")