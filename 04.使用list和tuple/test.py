# list test
classmates = ['Micheal', 'Bob', 'Tracy']

classmates.append('Adam')

classmates.insert(1, 'Jack')

tmp = classmates.pop(1)

print("classmates:", classmates, '\nlen=%d' % len(classmates))

print(tmp)


# tuple test
classtuple = ('Micheal', 'Bob', 'Tracy')
tuple1 = (1, ['Micheal', 'Bob', 'Tracy'])

print(classtuple, tuple1, tuple1[1][2])

# practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
