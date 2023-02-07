#task1
class InputOutputString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

str_obj = InputOutputString()
str_obj.get_string()
str_obj.print_string()

#task2
class Shape:
    def area(self, length:int):
        self.length = length
        length = 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length**2)
n = int(input())
x = Square(n)
x.area()

#task3
class Shape:
    def area(self, length:int, width:int):
        self.length = length
        self.width = width
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)
n = int(input())
m = int(input())
x = Rectangle(n,m)
x.area()

#task4
import math   
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = abs(other.x - self.x)
        dy = abs(other.y - self.y)

        return math.sqrt(dx * dx + dy * dy)

    
    def __str__(self):
        return f'Point (x = {self.x}, y = {self.y})'

point1 = Point(10, 4)
print(point1)
print(point1.get_x())
print(point1.get_y())
point1.move(10, 1)
print(point1)
point2 = Point(6,7)
print(point1.dist(point2))
#task5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f'Your balance: {self.balance}')
    def withdraw(self, amount):
        if amount > self.balance:
         print('You can`t withdraw')
        else:
         self.balance -= amount
         print(f'Your balance after withdrawal: {self.balance}')
acct = Account('Arman', 1000)
acct.deposit(500)
acct.withdraw(423)
acct.withdraw(342)
#task6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [3, 4, 6, 11, 12, 17, 18, 20, 23]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
