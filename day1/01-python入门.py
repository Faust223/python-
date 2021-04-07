print("hello,world!")

# 1.字符串
name = "xxx"
print(name,type(name))

#2.整形
age =12
print(age,type(age))

# 3.小数
salary = 23.5
print(salary,type(salary))

# 4.初始值是同一个值
f1=f2=f3=f4=f5=100

# 5.变量重新赋值
num =12
num = "xxxx"
print(num,type(num))

# 6.变量
print()

# 7.扩展：交换两个数的值
a=100
b=200

#方式一：中间变量
t=a
a=b
b=t

#方式二：解包赋值
a,b=b,a

# 8.输入输出 input
# 注意：但凡通过input输入的数据类型，都是字符串类型
inputAge=input("请输入你的年龄")

# 9.强制类型转换 例如：int(xx) 转换为int类型 float(xx)转换为float类型 str(xx)转换为字符窜类型
ages= int(inputAge)
age_str = str(ages)
age_float = str(age_str)
print(age_float,type(age_float))