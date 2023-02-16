#task1
import re
str1 = input()
def test(str1):
    if re.search('a(b*)', str1):
     print('Yes')
    else:
     print('No')  

test(str1)

#task2
import re
str1 = input()
def test(str1):
    if re.search("(a)b{2,3}", str1):
        print('Yes')
    else:
        print('No')

test(str1)

#task3
import re
str1 = input()
def lower_under(str1):
    pattern = r'[a-z]+_[a-z]+\b'
    str2 = re.findall(pattern, str1)
    return str2

print(lower_under(str1))

#task4
import re
str1 = input()
def sequence(str1):
    pattern = r'[A-Z][a-z]+'
    str2 = re.findall(pattern, str1)
    return str2

print(sequence(str1))

#task5
import re
str1 = input()
def test(str1):
    if re.search('a()b$', str1):
        print('Yes')
    else:
        print('No')
test(str1)

#task6
import re
str1 = input()
pattern = '\s+'
pattern1 = '\,'
pattern2 = '\.'
replace = ':'
str2 = re.sub(pattern, replace, str1)
str2 = re.sub(pattern1, replace, str2)
str2 = re.sub(pattern2, replace, str2)
print(str2)

#task7
import re
str1 = input()
def snakeToCamel(str1):
    result = ''.join(x.capitalize() or '_' for x in str1.split('_'))
    print(result)
snakeToCamel(str1)

#task8
import re
str1 = input()
def split(str1):
    str2 = re.findall('[A-Z][^A-Z]*', str1)
    return ' '.join(str2)
print(split(str1))

#task9
import re
str1 = input()
def insertSpaces(str1):
    str2 = re.sub(r"(?<!^)(?=[A-Z])", " ", str1)
    print(str2)
insertSpaces(str1)

#task10
import re
str1 = input()
def camel_to_snake(str1):
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', str1).lower()
    print(result)

camel_to_snake(str1)