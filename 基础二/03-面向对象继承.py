# 继承 父类 子类
class Father:
    age = 20
    __b = 10

    def show(self):
        print("父类方法...")


class Son(Father):

    def learn(self):
        print("子类进行学习...")


# 子类继承父类，会继承父类的属性和方法，但是私有属性除外
# 子类
# 创建子类对象
s = Son()

# 创建子类自己方法
s.learn()

# 子类调用父类的方法和属性
s.age = 18
s.learn()
