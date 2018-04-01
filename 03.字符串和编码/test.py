
print(ord('中'), ord('文'), chr(66), chr(25991),  '\u4e2d\u6587')


# '中文'.encode('utf-8'), '1234556'.encode('ascii')
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))


print('%2d - %04d' % (3, 1))
print('%s %.2f' % ('pi=', 3.1415))


s1 = 72
s2 = 85

r = ((s2-s1)/s1) * 100

print('小明成绩上升%.1f%%' % r)

