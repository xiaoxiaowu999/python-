# 函数执行完毕也没有return语句时，自动return None

from abstest import my_abs
print(my_abs(-9))

# practice

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。


def quadratic(a, b, c):
    import math
    if not isinstance(a, (int, float)):
        raise TypeError('数据类型错误')
    elif not isinstance(b, (int, float)):
        raise TypeError('数据类型错误')
    elif not isinstance(c, (int, float)):
        raise TypeError('数据类型错误')
    d = b * b - 4 * a * c
    if a == 0:
        print('a值不能为0')
    x1 = (-b + math.sqrt(d)) / 2 / a
    x2 = (-b - math.sqrt(d)) / 2 / a
    return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
