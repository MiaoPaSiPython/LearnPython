# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:31
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : oop_objvar.py
# @Software: PyCharm

class Robot:
    """表示有一个带有名字的机器人。"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人
        # 将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

'''
how_many 实际上是一个属于类而非属于对象的方法。
这就意味着我们可以将它定义为一个 classmethod（类方法） 或是
一个 staticmethod（静态方法），这取决于我们是否需要知道这一方法属于哪个类。
由于我们已经引用了一个类变量，因此我们使用 classmethod（类方法）。

我们使用装饰器（Decorator）将 how_many 方法标记为类方法。

你可以将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式，
因此启用 @classmethod 装饰器等价于调用：

how_many = classmethod(how_many)



'''