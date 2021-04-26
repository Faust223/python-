import csv
import jieba
from PIL import Image
from wordcloud import WordCloud
import numpy as np

# 1.读取csv文件
def readMeantor():

    with open("./data/mentor_paper.csv","r",encoding='utf-8')as file:
        csvReader = csv.reader(file)
        list_mentor=[i for i in csvReader]
        list_filter = [mentor for mentor in list_mentor if("地质" in mentor[3])]
        return list_mentor

# 2.将读取的数据进行分词
def downPicture():
    # 将所有标题整合成为一个字符窜
    finalTitle = ""
    for mentor in list_mentor:
        finalTitle += mentor[3]
    # 分词
    result = jieba.cut(finalTitle)

    # 读取图片
    img = Image.open("三角形.png")

    # 生成词云图
    wordCloud = WordCloud(
        font_path="方正粗黑宋简体.ttf",
        background_color='white',
        mask=np.array(img)
    ).generate(finalTitle)

    # 图片
    wordCloud.to_file("导师课题分析.png")


if __name__ == '__main__':
    # 读取csv文件（知网爬取的数据）
    list_mentor = readMeantor()
    # 生成词云图
    downPicture()












