#数据类型
# 1.数字 int/float

n1=10
n2=12.3

# 2.字符串：str
str1 ="12"
str2='xxx'
str3 = '''xxx'''
str4 = """xxx"""


# 3.布尔值类型：bool
b1 = True
b2 = False

# 4.列表：list
# 特点：有序的，允许重复元素，允许不同类型数据
score_list=[11,22,33,'xxx']
print(score_list)

# 列表添加数据：
# 1.insert：根据下标向指定位置添加元素
# 2.append: 向列表末尾添加元素

score_list.append("城市学院")
score_list.insert(2,13)

# 根据下标查询列表中的数据
# 下标范围：可为-1，-2，-3...

print(score_list[-1])

# 根据下标修改
score_list[0]=111
print(score_list)

# 根据下标删除元素
del score_list[0]
print(score_list)

# 直接删除整个列表
# del score_list

# 列表之间可以用+拼接
listAll = score_list+['4',True,False,"GA",23.322]
print(listAll)

# 5.元组
# 特点：有序的，元素可以重复，元素可以不同类型，但是，不可以添加元素，修改元素，删除元素。

# 6.字典 dict
# 字典中的元素都是key，value的组合形式，都是成对出现的，键值对
# key值是不能重复的
# value可以重复
student1 ={"name":"xxxtentacion","age":20}
print(student1,type(student1))

# （1）.根据查询元素
print(student1['name'])

# （2）.根据key修改元素
student1['name'] = 'juice'
print(student1)

# （3）.根据值删除元素
del student1['name']
print(student1)

# （4）.添加元素
student1['address'] = 'American'
print(student1)

# 6.集合 set
# 无序的，元素不可以重复（重复会被覆盖），允许数据类型不同
# student={} 默认是字典
student_set = {"xxx","xxx",23.33,True}
print(student_set)
print(type(student_set))

































