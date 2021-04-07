from selenium import webdriver
'''
一、selenium库介绍:
1.web自动化测试工具
2.配合chromeDriver使用

二、安装
1.chromeDriver下载（驱动与浏览器版本要接近）：
http://npm.taobao.org/mirrors/chromedriver/

2.方法一，解压放入python/script/文件夹下（.exe文件）
方法二，直接放在项目文件夹下

3.from selenium import webdriver（没有报错就算成功）

'''


url = "http://www.baidu.com.cn"



# 1.获取浏览器对象
# webdriver.Chrome(executable_path='chromedriver.exe')

brower = webdriver.Chrome()

# 2.窗口最大化
brower.maximize_window()

# 3.使用浏览器打开url
brower.get(url)

# 4.获取当前网页的源代码
# print(brower.page_soutce)

# 5.根据选择器找到输入框
brower.find_element_by_css_selector("#kw").send_keys("xxxtentacion")

# 6.找到搜索框并点击
brower.find_element_by_css_selector("#su").click()

# 7.清空输入框
brower.find_element_by_css_selector("#kw").clear()

# 8.根据选择器找到输入框，输入小果汁
brower.find_element_by_css_selector("#kw").send_keys("juice wrld")

# 9.找到搜索框并点击
brower.find_element_by_css_selector("#su").click()













