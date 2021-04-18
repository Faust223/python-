# 文件读取
# 结论
# 1.pycharm工具默认的字符编码：utf-8
# 2.encoding 是设置字符集编码的
# 3. encoding :文件读写的编码方式，默认是gbk读取


# 1.打开文件

fileRead = open("./文件/read.txt", "r", encoding="utf-8")
# 调用读取方法
result = fileRead.readlines()

print(type(result))


# 2.区分文件读写是常用的方法
# readline:每次只读取一行
# readlines：读取所有内容，返回每行内容作为元素组成的列表

# 打开文件
fileRead = open("./文件/read.txt", "r",encoding="utf-8")

# 调用读取的方法
result = fileRead.readline()
print(type(result))







