#task1
def squares(max = 0):
    n = 1
    while n <= max:
        yield n ** 2
        n +=1
a = squares(int(input()))

for i in a:
    print(i)

#task2
def evens(max = 0):
    n = int(input())
    for i in range(n):
        if i % 2 == 0:
         yield i
a = evens()
for i in a:
    print(i, sep = ", ")

#task3
n = int(input())
def div(n):
    for i in range(0, n+1):
        if i%3 == 0 or i%4 == 0:
         yield i
         i+=1
a = div(n)
for i in a:
    print(i)

#task4
a = int(input())
b = int(input())
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
        i+=1
x = squares(a,b)
for i in x:
    print(i)

#task5
def down(max = 0):
    n = int(input())
    while n >= max:
        yield n
        n -=1
a = down()
for i in a:
    print(i)