import pandas as pd
from pandas import DataFrame, Series
import requests
from bs4 import BeautifulSoup
import csv


# url = 'https://movie.douban.com/subject/33440021/reviews?start={}'

# 定义方法获取短评的作者 评分 内容
def getInfoByURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.141 Safari/537.36 "

    }

    # 1.携带请求头进行请求
    response = requests.get(url, headers=header)

    # 2.使用bs4和html5lib解析网页
    bs4 = BeautifulSoup(response.content, "html5lib")

    # 3.获取div
    divs = bs4.find("div", attrs={"id": "comments"})
    # 4.获取每一个小的div
    divList = divs.find_all("div", attrs={"class": "comment-item"})
    for item in divList:
        # 5.获取span 获取作者 评分
        spanAll = item.find("span", attrs={"class": "comment-info"})

        # 6.获取a标签中的作者名称
        author = spanAll.find("a").text

        # 7.获取评分
        rating = spanAll.find("span", attrs={"class": "rating"})

        # 判断
        if rating != None:
            # 评分
            star = rating.get("title")
            # 内容
            commentText = item.find("span", attrs={"class": "short"}).text.replace("\n", "")
            zidian = {"author": author, "star": star, "conment": commentText}
            commentData.append(zidian)




# 程序的入口
if __name__ == '__main__':
    commentData = []
    baseUrl = "https://movie.douban.com/subject/34841067/comments?start= {}&limit=20&status=P&sort=new_score"
    for i in range(0, 10):
        getInfoByURL(baseUrl.format(i * 20))
    df = DataFrame(
        data=commentData
    )
    # 写入csv文件
    #df.to_csv("豆瓣影评.csv", names=["author", "star", "comment"])
    # 读取
    data = pd.read_csv("豆瓣影评.csv", names=["author", "star", "comment"])
    print(data)