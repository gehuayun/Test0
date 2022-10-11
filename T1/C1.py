"""
新的python题目
开始执行···
正在进行···
"""
import random


def random_come():
    """
    随机数生成
    挑兵点将
    :return:
    """
    randomValue = random.randint(1, 10)
    print(randomValue)
    if randomValue == 1:
        print("关羽")
    elif randomValue == 2:
        print("张飞")
    elif randomValue == 3:
        print("赵云")
    elif randomValue == 4:
        print("马超")
    else:
        print("黄忠")
    print("五虎将")


def random_sum(co):
    if co == "+":
        """
         随机数积累相加
        :return:
        """
        random.Values = random.randint(10, 100)
        print(random.Values)
        sum1 = 0
        for i in range(1, random.Values + 1):
            sum1 += i
        print(sum1)
    elif co == "*":
        """
        随机数阶乘
        """
        random.Values = random.randint(5, 10)
        print(random.Values)
        sum1 = 1
        for i in range(1, random.Values + 1):
            sum1 *= i
        print(sum1)
    else:
        print("错误输入，请重试！！！")


def group_by():
    global var1
    var1 = []
    """
    1-4三位数分类组合
    不重复组合
    """

    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if a != b and c != b and a != c:
                    var1.append(100 * a + 10 * b + 1 * c)
    print(var1)
    print(len(var1))


def group_up():
    """
    编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））。
    获得的数字应以逗号分隔的顺序打印在一行上。
    :return:
    """
    global group1
    group1 = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            group1.append(i)
    print(group1)


if __name__ == "__main__":
    # random_come()
    # random_sum("+")
    # group_by()
    group_up()