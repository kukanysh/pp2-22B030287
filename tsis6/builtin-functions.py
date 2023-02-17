#task1
list1 = [2, 3, 4, 5]
sum = 1
for i in range(len(list1)):
    sum*=list1[i]
    i += 1
print(sum)

#task2
str1 = input()
def countUpLow(str1):
    count1 = 0
    count2 = 0
    for i in range(0, len(str1)):
        if str1[i].isupper():
         count1 += 1
        if str1[i].islower():
         count2 += 1
    print(f'Number of upper cases: {count1}')
    print(f'Number of lower cases: {count2}')

countUpLow(str1)

#task3
str1 = input()
str2 = str1[::-1]
if str2 == str1:
    print('Palindrome')
else:
    print('Not palindrome')

#task4
import math
print('Sample Input:')
num = int(input())
time = int(input())
sqrt = math.sqrt(num)
print('Sample Output:')
print(f'Square root of {num} after {time} miliseconds is {sqrt}')

#task5
tup1 = input()
def true_tup(tup1):
    return all(tup1)
print(true_tup(tup1))