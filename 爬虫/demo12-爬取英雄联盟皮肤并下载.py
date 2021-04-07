import requests
import urllib.request as req
import os

'''
英雄列表的url地址
    # 英雄列表的url地址
    heroListUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    # 英雄详情的url地址
    heroInfoUrl = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
    
    思路：
    1.获取所有英雄的id，展示所有英雄的id和名称
    2.用户手动输入要下载皮肤的英雄id，我们再下载
    
'''

# 1.获取所有英雄的id，展示所有英雄的id和名称
def getHeroInfo():
    # 1.发送请求
    heroList=requests.get(heroListUrl).json()['hero']
    # 2.循环遍历获取每个英雄
    i=0
    for hero in heroList:
        heros.append(hero['heroId'])
        print(hero['heroId'],hero['name'],end="\t\t")
        i+=1
        if i==5:
            print("")   # 换行
            i=0
# 2.用户手动输入要下载皮肤的英雄id，我们再下载
def downloadSkinById():
    # 1.获取用户输入的id
    inputId = input("请输入您要下载的英雄的id：")
    # 2.判断输入的id是否存在
    # in :在...里
    if inputId in heros:
        # 3.根据输入的id组成英雄详情的url来发送请求
        skins=requests.get(heroInfoUrl.format(inputId)).json()['skins']
        print("您要下载的皮肤总计{}个".format(len(skins)))
        # 4.获取英雄名字，并作为文件夹的名字
        heroName=skins[0]['heroName']
        if not os.path.exists(heroName):
            os.mkdir(heroName)
        # 5.循环遍历
        for skin in skins:
            # 获取皮肤名称
            skinName = skin['name']
            # 判断如果mainImg是不是为空，如果不为空考研下载，下载炫彩皮肤chromaImg
            if skin['mainImg']!="":
                req.urlretrieve(skin['mainImg'],"{}/{}.jpg".format(heroName,skinName))
            else:
                req.urlretrieve(skin['chromaImg'],"{}/{}.jpg".format(heroName,skinName))
            print("{}的{}皮肤下载成功".format(heroName,skinName))
    else:
        print("您输入的id不存在，请重新输入。")


# 菜单
def menu():
    # 展示所有英雄的id和名称
    getHeroInfo()
    print("")   # 换行
    # 用户手动输入要下载皮肤的英雄id，我们再下载
    downloadSkinById()
    # 为了让用户体验更好，y：继续 n：退出
    yesOrNo = input("请输入：y：继续 n：退出")
    if yesOrNo=='y':
        menu()
    elif yesOrNo=='n':
        print("程序退出......")






# 程序入口
if __name__=='__main__':
    print("-----------------英雄id和英雄名称-------------------")
    # 英雄列表的url地址
    heroListUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    # 英雄详情的url地址
    heroInfoUrl = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
    # 定义一存储英雄id和名称的空列表
    heros=[]
    menu()

