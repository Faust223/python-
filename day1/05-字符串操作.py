msg = "《文章》包括各种文体的著作、作品，如诗歌、戏剧、小说、科学论文，记叙文、议论文、说明文、应用文等等。"
# 1.split：字符串的分割，返回结果是一个列表
res = msg.split("、")

# 2.strip():对切割后的列表数据循环输出并去掉空格
for item in res:
    print(item.strip()) #去掉首尾空格

# 3.replace（）：字符串替换
word = "xxxtentacion"
word = word.replace("xxx",'XXX').replace("t","T") # 链式操作
print(word)

# 4.strip：去掉首尾空格
msg2 = " hello,world "
msg2 = msg2.replace(" ","")
print(msg2)

# 5.find():查找一个字符串是否存在字符
msg3 = "helloworld"
ms = msg3.find("x")
print(ms)








