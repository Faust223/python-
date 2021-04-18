
# 导入正则库
import re

# [abc] 可以匹配a,b,c

# 正则表达式常用方法
# 1.match：只满足正则的第一个匹配结果，第一个字符必须满足，否则为None
result = re.match(r'[abc]', 'a12345bc')
# match结果为为对象，想要得到匹配结果，就要使用group()方法
print(type(result))
print(result.group())

# 2.findall():结果返回一个列表
result = re.findall(r'[abc]', 'a123456bc')
print(type(result))
print(result)

# search:和match效果一样，但是，可以允许第一个字符不匹配
result = re.search(r'[abc]', " 123abc123456")
print(type(result))
print(result.group())




