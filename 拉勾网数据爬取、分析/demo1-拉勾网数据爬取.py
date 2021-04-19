from idlelib import browser
from selenium import webdriver
import time
import csv


def getDate():
    # 3.发送请求
    browser.get(url)
    # 4.定位全国
    browser.find_element_by_css_selector("#changeCityBox > p.checkTips > a").click()
    # 5.找到文本框输入数据分析
    browser.find_element_by_css_selector("#search_input").send_keys("数据分析")
    # 6.找到搜索按钮并点击
    browser.find_element_by_css_selector("#search_button").click()
    time.sleep(3)
    # 7.自动翻页 pager_next_disabled pager_next
    i = 1
    # 控制页数
    j = 1
    # 控制条数
    while (browser.page_source.find('pager_next_disabled') == -1):
        # 找到li
        li_List = browser.find_elements_by_css_selector("#s_position_list > ul > li")
        # 循环遍历 123456789101112131415161718192021
        for li in li_List:
            # 标题
            title = li.find_element_by_css_selector("div.list_item_top > div.position > div.p_top > a > h3").text
            # 地址
            address = \
            li.find_element_by_css_selector("div.list_item_top > div.position > div.p_top > a > span > em").text.split(
                "·")[0]
            # 公司
            company = li.find_element_by_css_selector("div.list_item_top > div.company > div.company_name > a").text
            # 薪水，经验
            result = li.find_element_by_css_selector("div.list_item_top > div.position > div.p_bot > div").text
            # 薪水
            salary = result.split(" ")[0]
            # 经验
            exp = result.split(" ")[1].replace("经验", "")
            # 学历
            edu = result.split(" ")[-1]
            # 类型
            type = li.find_element_by_class_name("industry").text.split("/")[0].strip()
            # 写入cvs
            with open("lagou_date.cvs", "a", encoding="utf-8", newline="") as file:
                csvWriter = csv.writer(file).writerow([title, address, company, salary, exp, edu, type])
                print("第{}页第{}条下载成功".format(i, j))
                j += 1
                # 找到 下一页点击
        browser.find_element_by_class_name("pager_next").click()
        i += 1
        time.sleep(3)


if __name__ == '__main__':
    # 1.获取浏览器对象
    browser = webdriver.Chrome()
    # 2.窗口最大化
    browser.maximize_window()
    url = "https://www.lagou.com/"
    getDate()
