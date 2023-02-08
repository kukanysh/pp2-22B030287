#task1
def getOun(gramm):
   return gramm * 28.33

print(getOun(10000))

#task2
temp =int(input())
def FarToCel(temp):
    return (temp-32)*(5/9)

print(FarToCel(temp))

#task3
numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    
    for x in range(numheads+1):
        y = numheads - x
        if (x*2)+(y*4) == numlegs:
            return x, y

print(solve(numheads, numlegs))

#task4
def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

numbers = [int(num) for num in input().split()]
primes = filter_prime(numbers)
print("Prime numbers:", primes)

#task5
def permutation(string):
    if len(string) == 0:
        return ['']
    prev_list = permutation(string[1:len(string)])
    next_list = []
    for i in range(len(prev_list)):
        for j in range(len(string)):
            new_string = prev_list[i][0: j] + string[0] + prev_list[i][j: len(string) - 1]
            if new_string not in next_list:
                next_list.append(new_string)
    return next_list

input_string = input()
result = permutation(input_string)
for item in result:
    print(item)

#task6
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

sentence = input()
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)

#task7
def has_33(nums):
     s = ""
     for i in nums:
         s += str(i)
     return "33" in s
nums = list(input().split(", "))
print(has_33(nums))

#task8
def spy_game(nums):
    s = [0,0,7,'x']
    for i in nums:
        if i == s[0]:
         s.pop(0)
        if len(s) == 1:
            return True
    return False
nums = list(map(float,input().strip().split(",")))
print(spy_game(nums))

#task9
r = int(input())
def volumeSphere(r):
    return (r**3)*(4/3)* 3.14
print(volumeSphere(r))

#task10
list1 = list(input().split(","))
def unique(list1):
    uniqueElements = []
    for i in list1:
        if i not in uniqueElements:
            uniqueElements.append(i)
    return uniqueElements
uniqueElements = unique(list1)
print(uniqueElements)

#task11
word = input()
def pal(word):
    word1 = "".join(reversed(word))
    if word1 == word:
     print("palindrome")
    else:
     print("not palindrome")
pal(word)

#task12
list1 = list(input().split(", "))
def histogram(list1):
    for number in list1:
        print('*'*int(number))
histogram(list1)

#task13
import random

def guessnumber():
    number = random.randint(1, 20)
    print('What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    print('Take a guess')
    attempts = 0
    
    while True:
        guess = int(input())
        attempts+=1
        if number == guess:
         print(f'Good job, {name}! You guessed my number in {attempts} guesses!')
        elif number > guess:
         print('Your guess is too low')
         print('Take a guess.')
        else:
         print('Your guess is too high')
         print('Take a guess.')
guessnumber()


