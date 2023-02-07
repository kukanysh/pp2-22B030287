#task1
class S:
    def getString(self, name):
        return name
    def printString(self, name):
        print(self.getString(name))
s = S()
str1 = input()
s.printString(getString(str1))
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
def getOun(gramm):
   return gramm * 28.33

print(getOun(10000))

#task4
def getContains(list1):
     s = ""
     for i in list1:
         s += str(i)
     return "33" in s
print(getContains([1, 2, 3, 3, 5, 9, 33, 534]))
