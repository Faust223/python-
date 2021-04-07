import requests
import re

# 1.url地址
url = "https://sc.chinaz.com/tupian/210108513030.htm"

# 2.使用请求库向url请求，并接受请求
# response.status_code:响应的状态码：200成功
# response.text:获取响应的源内容（网页源代码）字符串类型（一般会乱码）
# response.content:获取响应的源内容，二进制内容


response = requests.get(url)
# print(response.content.decode())

# 3.将读取到的内容写入文件
with open("picture.html", "wb") as file:
    file.write(response.content)
'''
<img src="//scpic.chinaz.net//files/pic/pic9/202012/apic29961_s.jpg"  alt="超短牛仔裤亚洲美女图片" class="preview">
<img src = "//scpic.chinaz.net//files/pic/pic9/202101/apic30015_s.jpg"alt = "优雅气质亚洲美女写真图片"class ="preview" >
<img src="//scpic.chinaz.net//files/pic/pic9/202101/apic30020_s.jpg"  alt="亚洲唯美黑白艺术照" class="preview">
<img src="//scpic.chinaz.net//files/pic/pic9/202101/apic30011_s.jpg"  alt="欧洲轻熟风美女少妇图片" class="preview">
'''

# 4.正则表达式
msg = '<img src=".*" alt=".*">'

# 5.测试正则
result = re.findall(r'<img src="(.*)">' , '<img src="//scpic.chinaz.net//files/pic/pic9/202101/apic30011_s.jpg"  alt="欧洲轻熟风美女少妇图片" class="preview">')

# 6.读取picture.html的所有内容，然后使用正则表达式提取图片路径
with open('picture.html', "r", encoding="utf-8") as files:
    html = files.read()
imgUrlList = re.findall(r'<img src="(.*)">', html)
print(imgUrlList,len(imgUrlList))
