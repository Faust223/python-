from selenium import webdriver
import csv

# 一、处理csv数据

list_mentor = []
# 1.先打开文件
file = open("./data/Mentor.csv", "r", encoding="utf-8")
str_mentor = file.read()

# 2.去除导师名单里的空格
str_mentor = str_mentor.replace(" ", "")

# 3.以、分隔每位导师
list_mentor = str_mentor.split("、")

# 二、数据爬取

# 1.知网网站
url = "http://42.192.159.244:8081//kns/brief/default_result.aspx"

# 2.获取浏览器对象
brower = webdriver.Chrome()

# 3.使用浏览器打开url
brower.get(url)

# 4.找到筛选条件一：作者
brower.find_element_by_css_selector("#txt_1_sel > option:nth-child(4)").click()

# 遍历每位导师
for mentor in list_mentor:

    # 5.根据选择器找到输入框
    brower.find_element_by_css_selector('#txt_1_value1').send_keys(mentor)
    # 6.找到搜索框并点击
    brower.find_element_by_css_selector("#btnSearch").click()
    # 7.清除搜索框里数据
    brower.find_element_by_css_selector('#txt_1_value1').clear()

    # 8.先定位iframe的位置
    li = brower.find_element_by_css_selector('#iframeResult')
    # iframe的问题：直接搜索iframe里面元素（报错：定位错误）
    # 终于找到问题了...iframe需要单独进入(switch_to.frame方法才算进入)
    #进入iframe里面
    brower.switch_to.frame(li)

    '''
    tbody > tr
    tr:
    #ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody > tr.GTContentTitle
    #ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2)
    #ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3)
    #ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4)
                                   控制每条数据                       控制每条数据里的每个元素
    '''

    try:
        author = []
        count_f = 1  # 控制一行里面的每个元素变化
        count = 2  # 控制每行的变化
        i = 1
        while (True):
            # tbody装着每一页的所有tr（一页20条）
            list_tbody = brower.find_element_by_css_selector(
                "#ctl00 > table > tbody > tr:nth-child(2) > td > table > tbody")
            # 标题
            title = list_tbody.find_element_by_css_selector(
                "tr:nth-child(" + str(count) + ")" + " > td:nth-child(2) > a").text
            # 链接
            link = list_tbody.find_element_by_css_selector(
                "tr:nth-child(" + str(count) + ")" + " > td:nth-child(2) > a").get_attribute('href')
            # 作者（多个）
            try:
                while (True):
                    author.append(list_tbody.find_element_by_css_selector(
                        "tr:nth-child(" + str(count) + ")" + "> td:nth-child(3) > a:nth-child(" + str(
                            count_f) + ")").text)
                    count_f += 1
            except Exception:
                print("作者寻找完毕！")
            # 来源
            source = list_tbody.find_element_by_css_selector(
                "tr:nth-child(" + str(count) + ")" + "> td:nth-child(4) > a").text
            # 时间
            time = list_tbody.find_element_by_css_selector(
                "tr:nth-child(" + str(count) + ")" + "> td:nth-child(5)").text
            # 写入csv文件
            with open("./data/mentor_paper.csv", "a", newline="", encoding='utf-8') as file:
                csv.writer(file).writerow([title, link, author, source, time])
            print("{}结果的第{}条下载成功".format(mentor, i))
            i += 1
            count += 1

    except Exception:
        print("遍历完毕！")
    # 退出iframe（否则会定位不到iframe外的元素）
    brower.switch_to.default_content()

'''
1.不能分页爬取
2.最后根据爬取完的数据再数据分析，筛选，清洗，最后，下载。


'''
# 关闭浏览器
brower.close()
