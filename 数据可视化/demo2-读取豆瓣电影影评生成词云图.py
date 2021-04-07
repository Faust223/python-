import jieba
from wordcloud import WordCloud
import csv
import numpy as np
from PIL import Image


# 思路：1.先读取豆瓣影评 2.将读取的内容分词 3.生成词云图

# 先读取豆瓣影评
def readerComment():
    with open("豆瓣影评.csv", "r", encoding="utf-8") as file:
        csvReader = csv.reader(file)
        # for item in csvReader:
        #     print(item[2])
        return [item[2] for item in csvReader]


# 2.将读取的内容分词
def downPicture():
    # 将所有的评论整合为一个字符窜
    finalComment = ""
    for comment in commentList:
        finalComment += comment
    # 分词
    result = jieba.cut(finalComment)

    # 读取图片
    images = Image.open("白雪公主2.png")

    # 生成词云图
    wordCloud = WordCloud(
        font_path="方正粗黑宋简体.ttf",
        background_color="white",
        mask=np.array(images)

    ).generate(finalComment)
    # 图片
    wordCloud.to_file("豆瓣影评词云图.png")


if __name__ == '__main__':
    commentList = readerComment()
    # 生成词云图
    downPicture()

'''
作业：
pyecharts文档
课程进度：

1.数据可视化
2.数据清洗，分析

'''
