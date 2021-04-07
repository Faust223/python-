# 英雄联盟数据集合json分析
# 标题：抓取英雄联盟内容并写入csv文件中
import csv
import requests
from bs4 import BeautifulSoup

'''
# 英雄列表的地址
heroList="https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"

# 英雄详情的地址
heroInfoList = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js" {}：为英雄的id


结果：获取每个英雄详情并存入csv文件中
思路：1.先获取每个英雄
2.根据英雄的id获取对应英雄的详情url地址
3.通过请求英雄详情地址就获取对应英雄详情信息
4.把信息存入csv中
'''


# 定义方法获取每个英雄的id
def getHeroId():
    # 1.向英雄列表的url地址发送请求
    heroList = requests.get(heroListUrl).json()['hero']
    # heroId = []
    # 2.遍历 获取每个英雄
    # for hero in heroList:
    #     heroId.append(hero['heroId'])
    # print(heroId)
    return [hero['heroId'] for hero in heroList]  # 列表生成式


# 定义方法通过英雄id获取英雄详情并写入csv文件中
def getHeroInfo():
    # 遍历所有的英雄id
    for heroId in heroIds:
        # 向英雄的详情url地址发送请求
        result = requests.get(heroInfoUrl.format(heroId)).json()['hero']
        # 获取英雄类容
        # id
        id = result['heroId']
        # name
        name = result['name']
        # 生命值
        hp = result['hp'] + "{}/级".format(result['hpperlevel'])
        # 护甲
        armor = result['armor'] + "{}/级".format(result['armorperlevel'])
        # 移速
        movespeed = result['movespeed']
        # 伤害
        attackdamage = result['attackdamage'] + "{}/级".format(result['attackdamage'])
        # 写入csv文件中
        with open("lol.csv", "a", encoding="utf-8", newline="")as files:
            csv.writer(files).writerow([id, name, armor, movespeed, attackdamage])


# python 中也有main方法，是程序入口
if __name__ == '__main__':
    # 英雄列表的url地址
    heroListUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    # 英雄详情的url地址
    heroInfoUrl = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'

    # 定义一个写入csv文件的标题
    with open("lol.csv", "a", encoding="utf-8", newline="") as file:
        csv.writer(file).writerow(['英雄id', '英雄名称', '生命值', '护甲', '移速', '伤害'])
    # 获取每个英雄的id
    heroIds = getHeroId()
    getHeroInfo()
