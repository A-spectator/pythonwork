


#14、python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy as np

a = random.randint(10, 20)
res = np.random.randn(5)
ret = random.random()
print("正整数:" + str(a))
print("5个随机小数:" + str(res))
print("0-1随机小数:" + str(ret))
