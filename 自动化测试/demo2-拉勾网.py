from selenium import webdriver

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
brower.find_element_by_css_selector("#search_input").send_keys("java")

# 7.点击搜索
brower.find_element_by_css_selector("#search_button").click()


# 8.清空输入框
brower.find_element_by_css_selector("#keyword").clear()

# 9.有问题
brower.find_element_by_css_selector("#keyword").send_keys("python")

# 10.点击搜索
brower.find_element_by_css_selector("#submit").click()

# 我在想电影里的：远程操控别人电脑打开软件。可以用在很多地方。