# 1.创建类
class Student:
    # 2.属性
    name = ""
    age = 20
    # 私有属性 python中定义私有属性（前面两个下划线） 不能在外部调用，仅内部使用
    __a = 200

    # 3.方法
    # self：当前对象

    def show(self, name, age):
        self.name = name
        self.age = age
        print("方法........", self.name, self.age)


# 类外部方法：
def test():
    print("测试外部方法")


# 创建对象

student = Student()

# 调用类中的属性和方法
student.name = "aa"
student.age = 20
student.show("xxxtentacion", 20)

# test前没tab，属于外部方法，不属于student类，不需要student.test()调用，直接调用

test()

# 私有属性外部不可以调用
# print(student.__a)

