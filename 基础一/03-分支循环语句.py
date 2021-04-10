# 1.分支：if
if 1:
    print("xxxtentacion")

num1 = input("请输入第一个数：")
num2 = input("请输入第二个数：")

# 单分支结构
if num1 >= num2:
    print(num1)

# 双分支结构:二选一
if num1>=num2:
    print(num1)
else:
    print(num2)

# 多分支：
if num1>num2:
    print(num1)
elif num2>num1:
    print(num2)
else :
    print("相等")

# 循环
# 使用循环遍历列表中的数据
rappers=['xxx','juice','uzi',True]
for item in rappers:
    print(item)

# 使用循环遍历取值：10以内的值
# range(a,b,c):取值范围：a到b（左闭右开区间），c是步长，默认是1
for i in range(10,20,2):
    print(i)

# 遍历10到20以内的所有数值存储在列表中
numList=[]
for i in range(10,20):
    numList.append(i)
print(numList)

# 列表生成式
numList2 = [i for i in range(10,20)]
print(numList2)













