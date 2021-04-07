import requests
from bs4 import BeautifulSoup
'''
https://lol.qq.com/data/info-heros.shtml
'''
url="https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"

# 使用bs4打印出来没有英雄列表数据，<li>里只有拼命加载中，原因是之前bs4爬取的是同步请求，是json格式，这是异步请求
# response = requests.get(url)
# bs4 = BeautifulSoup(response.content,"html5lib")
# print(bs4)
# json():将获取到的结果转换为json数据
# json数据可以当数字字典来使用
result = requests.get(url).json()['hero']
for hero in result:
    print(hero)
