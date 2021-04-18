class Student:

    # 初始化方法：不需要自己定义

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化方法....", self.name, self.age)

    def show(self):
        print("打印信息....")


# 创建对象

student = Student("xxx", 20)
student.show()
