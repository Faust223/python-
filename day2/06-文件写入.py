# 1.打开文件
fileWrite = open("./文件/write.txt", "w", encoding="utf-8")

# 2.调用写入的方法
# 没有文件，会自动创建
fileWrite.write("hello,world!号的按时付款")
fileWrite.close()

# 写完自动关闭
with open("./文件/write.txt","w",encoding="utf-8") as file:
    file.write("hello很好")

# 读取文件自动关闭
with open("./文件/write.txt","r",encoding="utf-8") as files:
    print(files.read())






