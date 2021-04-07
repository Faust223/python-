from selenium import webdriver
import csv
import os
import time

# 拉钩网点击弹出的广告
url2 = "https://www.lagou.com/"


# 1.获取浏览器对象
brower = webdriver.Chrome()

# 2.窗口最大化
brower.maximize_window()

# 3.使用浏览器打开url
brower.get(url2)

# 4.获取当前网页的源代码
# print(brower.page_soutce)

# 5.点击广告
brower.find_element_by_css_selector("#changeCityBox > p.checkTips > a").click()

# 6.输入java爬取职业数量
brower.find_element_by_css_selector("#search_input").send_keys("深度学习")

# 7.点击搜索
brower.find_element_by_css_selector("#search_button").click()

'''
相当于一个li装的所有信息：
#s_position_list > ul > li:nth-child(2)

下一页选择器（最后一页）：
#s_position_list > div.item_con_pager > div > span.



#J_bottomPage > span.p-num > a.pn-next.disabled

#J_goodsList > ul > li:nth-child(31)


#s_position_list > ul > li:nth-child(2) > div.list_item_top > div.position > div.p_top > a > h3
'''
time.sleep(2)

i = 1
j = 1
while(brower.page_source.find("pager_next.pager_next_disabled")==-1):
    li_list = brower.find_elements_by_css_selector("#s_position_list > ul > li")

    # 7.循环遍历
    for li in li_list:
        # 标签
        tag = li.find_element_by_css_selector("div.list_item_bot > div.li_b_l > span").text
        # 标题
        title = li.find_element_by_css_selector("div.list_item_top > div.position > div.p_top > a > h3").text
        # 工作经验
        work = li.find_element_by_css_selector("div.list_item_top > div.position > div.p_bot > div").text
        # print([start,title,price])
        with open("work.csv", "a", newline="", encoding='utf-8') as file:
            csv.writer(file).writerow([title, work, tag])
        print("第{}页第{}条下载成功".format(i,j))
        j+= 1
    brower.find_element_by_class_name("pager_next").click()
    i+=1
    time.sleep(2)

# 关闭浏览器
brower.close()