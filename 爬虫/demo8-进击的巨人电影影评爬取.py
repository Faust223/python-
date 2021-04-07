import requests
from bs4 import BeautifulSoup
import os

# url
#url = 'https://movie.douban.com/subject/33440021/reviews?start={}'

# 测试网页状态码
# for i in range(0,10):
#     reponse = requests.get(url)
#     print(reponse)

# 老师代码：《你好，李焕英》电影评论
import requests
from bs4 import BeautifulSoup
import csv

#定义方法获取短评的作者 评分 内容
def getInfoByURL(url):
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36" }

    # 1.携带请求头进行请求
    response=requests.get(url,headers=header)

    # 2. 使用bs4和html5lib解析网页
    bs4=BeautifulSoup(response.content,"html5lib")

    # 3.获取div 1234567891011121314
    divs=bs4.find("div",attrs={"id":"comments"})

    # 4.获取每一个小的div
    divList=divs.find_all("div",attrs={"class":"comment-item"})

    for item in divList:
        # 5.获取span 获取作者 评分
        spanAll = item.find("span", attrs={"class": "comment-info"})
        # 6.获取a标签中的作者名称
        author = spanAll.find("a").text
        # 7.获取评分
        rating=spanAll.find("span",attrs={"class":"rating"})
        # 判断
        if rating!=None:
            # 评分
            start=rating.get("title")
            #内容
            commentText=item.find("span",attrs={"class":"short"}).text
            print(commentText)
# 程序的入口
if __name__ == '__main__':
    baseUrl="https://movie.douban.com/subject/34841067/comments?start= {}&limit=20&status=P&sort=new_score"
    for i in range(0,10):
        getInfoByURL(baseUrl.format(i*20))
    # with open("a.csv", "w", encoding="utf-8", newline="") as file:
    #     csvWriter = csv.writer(file)

