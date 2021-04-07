import requests
import html5lib
from bs4 import BeautifulSoup
import os
import urllib.request as req
# 1.url
url = 'http://www.gaokao.com/e/20160201/56aed7e340aa9.shtml'

# 2.发送请求
reponse = requests.get(url)

# 测试是否200
# print(reponse)
'''
http://www.gaokao.com/e/20160201/56aed7e340aa9.shtml
http://www.gaokao.com/e/20160201/56aed7e340aa9_2.shtml
http://www.gaokao.com/e/20160201/56aed7e340aa9_3.shtml
http://www.gaokao.com/e/20160201/56aed7e340aa9_4.shtml
'''
# 创建文件夹
download = 'xiaohua1/'

# 如果不存在，则创建文件夹
if not os.path.exists(download):
    os.mkdir(download)


# 2.判断请求是否成功




















