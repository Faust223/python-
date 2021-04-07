import csv

from selenium import webdriver
import time

url='http://www.jd.com/'


# 1.获取浏览器对象
brower = webdriver.Chrome()

# 2.窗口最大化
brower.maximize_window()

# 3.使用浏览器打开url
brower.get(url)

# 4.输入男士衣服查找数据
brower.find_element_by_css_selector("#key").send_keys("男士衣服")

# 5.点击搜索按钮
brower.find_element_by_css_selector("#search > div > div.form > button").click()


# 延迟等待 网页是异步加载，所以得延迟跟网速有关
time.sleep(2)

# 使用循环，频繁翻页，频繁抓取，由于不知道具体多少页，所有用while
# 当下一页不能点击，循环结束
# #J_bottomPage > span.p-num > a.pn-next
# #J_bottomPage > span.p-num > a.pn-next.disabled
i = 1
j = 1
'''

价格：
#J_goodsList > ul > li.gl-item.hover > div > div.p-price > strong

名称：
#J_goodsList > ul > li.gl-item.hover > div > div.p-name.p-name-type-2 > a > em

店铺：
#J_goodsList > ul > li.gl-item.hover > div > div.p-shop > span > a

下一页按钮：
#J_bottomPage > span.p-num > a.pn-next > em
'''
while(brower.page_source.find("pn-next disabled")==-1):
    li_list = brower.find_elements_by_css_selector("#J_goodsList > ul > li")

    # 7.循环遍历
    for li in li_list:
        # 价格
        price = li.find_element_by_css_selector("div > div.p-price > strong > i").text
        # 标题
        title = li.find_element_by_css_selector("div > div.p-name.p-name-type-2 > a > em").text
        # 店铺 get_attribute("属性名称")：通过属性名来获得属性值
        start = li.find_element_by_css_selector("div > div.p-shop > span > a").get_attribute("title")
        # print([start,title,price])
        with open("男士衣服.csv", "a", newline="", encoding='utf-8') as file:
            csv.writer(file).writerow([start, title, price])
        print("第{}页第{}条下载成功".format(i,j))
        j+= 1
        # 用name？
    brower.find_element_by_class_name("pn-next").click()
    i+=1
    time.sleep(2)
