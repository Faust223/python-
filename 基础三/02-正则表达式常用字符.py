# 导入正则库
import re

# [abc] 可以匹配a、b、c
# abc
# ^ : 以...开头
# [^a-z]: 对小写字母取反
# $ :以...结尾
# \d : 等价于[0-9] \D：除了数字之外
# . :匹配除"\n"和"\r"之外的任何单个字符
result = re.findall(r'.', 'ab232Aage')
print(result)

# 正则表达式表示数量
# {m}: 表示前面字符数量为m个
# {m,n}: 表示至少查找m个，一直到n
# {m,}表示前面字符量至少为m个，一直到整个字符串结束
# + :表示前面字符数量为大于等于1次
# * ：表示前面字符串任意次（包含0次）
# | :或者
result = re.search(r'zo{5}','zoooooooss12')
print(result.group())


# 手机号匹配
# 正则匹配手机号：
result = re.findall(r'^1[3|5|8|9|7|]]\d{9}$', '13677103282')
print(result)






