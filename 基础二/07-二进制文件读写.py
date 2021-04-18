# 二进制读取时，不能添加encoding参数
with open("./文件/read.txt","rb") as file:
    # 把二进制文件内容转换为字符串内容：decode（）解码
    print(file.read().decode())

# 二进制文件写入
with open("./文件/write.txt","wb") as files:
    # 把字符串转换为二进制的字节数组：encode()编码
    files.write("age".encode())


# 二进制追加
with open("./文件/append.txt","ab") as fileAppend:
    fileAppend.write("嘻嘻".encode())


