# dict test
# dict 冒号前面没有空格，冒号后面要有空格
# dict内部存放的顺序和key放入的顺序是没有关系的
# key的对象就不能变
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

if 'Michael' in d:
    print('d has Michael')
# None 判断不要用==
if d.get('Thmos') is None:
    print('d don\'t has Thmos')

# set test
# set可以看成数学意义上的无序和无重复元素的集合
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print('s1与s2的交集：', (s1 & s2))

print('s1与s2的并集：', (s1 | s2))

# test

t1 = (1, 2, 3)
t2 = (1, [2, 3])

# this ok
d1 = {1: 45, t1: 12}
print('test1 ', d1)

# this error
d2 = {1: 45, t2: 12}
print('test2 ', d2)
