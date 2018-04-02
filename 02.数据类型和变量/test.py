# 这是我的注释

a = 1.235e8

if a >= 0:
    print(a)
else:
    print(-a)

print(r'''hello,\n
world''')

b1 = True
b2 = False

b3 = b1 and b2
print(b3)
b3 = b1 or b2
print(b3)
b3 = not b2
print(b3)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print('测试除法1\n', 10 / 3)
print('测试除法2\n', 10 // 3)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,\n
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)