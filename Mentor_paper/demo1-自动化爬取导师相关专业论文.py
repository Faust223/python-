from selenium import webdriver
import csv
import time

# 一、处理csv数据

list_mentor = []
# 1.先打开文件
file = open("./data/Mentor.csv", "r", encoding="utf-8")
str_mentor = file.read()

# 2.去除导师名单里的空格
str_mentor = str_mentor.replace(" ", "")

# 3.以、分隔每位导师
list_mentor = str_mentor.split("、")
#print(list_mentor)

# 二、数据爬取

# 1.知网网站
url = "http://42.192.159.244:8081//kns/brief/default_result.aspx"

# 2.获取浏览器对象
brower = webdriver.Chrome()

# 3.使用浏览器打开url
brower.get(url)

# 4.找到筛选条件一：作者
brower.find_element_by_css_selector("#txt_1_sel > option:nth-child(4)").click()



for mentor in list_mentor:

    try:
        # 5.根据选择器找到输入框
        brower.find_element_by_css_selector('#txt_1_value1').send_keys(mentor)
        # txt_1_value1
        # 6.找到搜索框并点击
        brower.find_element_by_css_selector("#btnSearch").click()
        # 7.清除搜索框里数据
        brower.find_element_by_css_selector('#txt_1_value1').clear()
        i = 1
        while True:

            count_y1 = 3
            count_y2 = 1
            j = 1

            author = []
            count_f = 1  # 控制第n个作者
            count = 2  # 控制每行的变化
            # 8.先定位iframe的位置
            li = brower.find_element_by_css_selector('#iframeResult')
            brower.switch_to.frame(li)
            time.sleep(1)
            try:
                while True:
                    # tbody装着每一页的所有tr（一页20条）
                    list_tbody = brower.find_element_by_css_selector(
                        "#ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody")
                    try:
                        # 标题
                        title = list_tbody.find_element_by_css_selector(
                            "tr:nth-child(" + str(count) + ")" + " > td:nth-child(2) > a").text
                    except Exception:
                        # 标题
                        title = list_tbody.find_element_by_css_selector(
                            "tr:nth-child(" + str(count) + ")" + " > td:nth-child(2)").text
                    # 链接
                    link = list_tbody.find_element_by_css_selector(
                        "tr:nth-child(" + str(count) + ")" + " > td:nth-child(2) > a").get_attribute('href')
                    # 作者（多个）
                    try:
                        while True:
                            author.append(list_tbody.find_element_by_css_selector(
                                "tr:nth-child(" + str(count) + ")" + "> td:nth-child(3) > a:nth-child(" + str(
                                    count_f) + ")").text)
                            count_f += 1
                    except Exception:
                        print("")
                    try:
                        # 来源
                        source = list_tbody.find_element_by_css_selector(
                            "tr:nth-child(" + str(count) + ")" + "> td:nth-child(4) > a").text
                    except Exception:
                        # 来源
                        source = list_tbody.find_element_by_css_selector(
                            "tr:nth-child(" + str(count) + ")" + "> td:nth-child(4)").text

                    # 时间
                    date_time = list_tbody.find_element_by_css_selector(
                        "tr:nth-child(" + str(count) + ")" + "> td:nth-child(5)").text
                    # 写入csv文件
                    with open("./data/mentor_paper_all.csv", "a", newline="", encoding='utf-8') as file:
                        csv.writer(file).writerow([title, link, author, source, date_time])
                    print("{}的论文第{}页第{}条下载成功".format(mentor, i, j))
                    j += 1
                    count += 1

            except Exception:
                print("一页爬取完毕！")
            if i==1:
                count_y1 = i+2
                brower.find_element_by_css_selector(
                    '#ctl00 > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td > div > a:nth-child(' + str(
                        count_y1) + ')').click()
                print("county1:",count_y1)
            else:
                count_y2=i+4
                brower.find_element_by_css_selector(
                    '#ctl00 > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td > div > a:nth-child(' + str(
                        count_y2) + ')').click()
                print("county2:",count_y2)

            # 退出iframe（否则会定位不到iframe外的元素）
            brower.switch_to.default_content()
            i += 1

    except Exception:
        # 退出iframe（否则会定位不到iframe外的元素）
        brower.switch_to.default_content()
        print("{}的所有论文结果爬取完毕！".format(mentor))

# 关闭浏览器
brower.close()

# # 分两种情况：
# 1.第一页：count=i+2开始
# 2.其他页：count=i+4开始
# i：当前页数
#


# 先看csv文件结果对不对（大概有300多行），再看报错的问题
# 为什么i恒为1？
#ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > a

# 现在问题在于：

'''
爬取的第二页是第五页内容

'''
