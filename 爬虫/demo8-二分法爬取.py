
import requests
from bs4 import BeautifulSoup
import csv
# url
#url = 'https://movie.douban.com/subject/33440021/reviews?start={}'

# 定义方法获取短评的作者 评分 内容
def getInfoByURL(url):
    header = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/87.0.4280.141 Safari/537.36 "

    }

    # 1.携带请求头进行请求
    response = requests.get(url,headers=header)

    # 2.使用bs4和html5lib解析网页
    bs4 = BeautifulSoup(response.content,"html5lib")

    # 3.获取div
    divs = bs4.find("div",attrs={"class":"review-list"})

    # 4.获取每一个小的div(里面是评论)
    divList = divs.find_all("div",attrs={"class":"main review-item"})

    for item in divList:
        # 5.获取span 获取作者 评分
        headerAll = item.find("header",attrs={"class":"main-hd"})

        # 6.获取a标签中的作者名称
        author = headerAll.find("a").text

        # 7.获取评分
        rating = headerAll.find("span",attrs={"class":"main-title-rating"})

        # 判断
        if rating!= None:
            # 评分
            star = rating.get("title")
            # 内容
            commentText = item.find("div", attrs={"class":"short-content"}).text
            with open("../python可视化/豆瓣影评.csv", "a", encoding="utf-8") as file:
                csvWriter = csv.writer(file)
                # 作者名字没爬到
                csvWriter.writerow([author, star, commentText])


# 程序的入口
if __name__ == '__main__':
    baseUrl = "https://movie.douban.com/subject/33440021/reviews?start={}"
    for i in range(0, 10):
        getInfoByURL(baseUrl.format(i*20))


