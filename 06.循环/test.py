names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)

# practice 1
sum = 0

for x in range(101):
    sum = sum + x

print(sum)

# practice 2
L = ['Bart', 'Lisa', 'Adam']
n = 0
while n < len(L):
    print('hello %s!' % L[n])
    n = n + 1

for l in L:
    print('hello %s!' % l)
