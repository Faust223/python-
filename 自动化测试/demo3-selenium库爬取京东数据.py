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

# 智能等待
# brower.implicitly_wait(100)

#print(brower.get_cookies())

# 延迟等待 网页是异步加载，所以得延迟跟网速有关
time.sleep(2)

# 获取网页源代码
#print(brower.page_source)

# 截图网页
#brower.get_screenshot_as_file("E:\Desktop\Python数据分析、挖掘与可视化\学习笔记\千锋python上课源码\img.png")

# 关闭单个页面
#brower.close()

# 关闭所有页面
# brower.quit()

# 6.获取li
'''
#J_goodsList > ul > li:nth-child(1)
'''
li_list = brower.find_elements_by_css_selector("#J_goodsList > ul > li")
i=1
# 7.循环遍历
for li in li_list:
    # 价格
    price = li.find_element_by_css_selector("div > div.p-price > strong > i").text
    # 标题
    title = li.find_element_by_css_selector("div > div.p-name.p-name-type-2 > a > em").text
    # 店铺 get_attribute("属性名称")：通过属性名来获得属性值
    start = li.find_element_by_css_selector("div > div.p-shop > span > a").get_attribute("title")
    #print([start,title,price])
    with open("男士衣服.csv","a",newline="",encoding='utf-8') as file:
        csv.writer(file).writerow([start,title,price])
    print("第{}条下载成功".format(i))
    i+=1



