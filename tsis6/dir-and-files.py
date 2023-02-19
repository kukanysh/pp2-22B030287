#task1
import os
path = '/Users/kuanysspandiar/pp2-22B030287'

print('Directories:')
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

print('\nFiles:')
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)
print('\nAll directories and files:')
for item in os.listdir(path):
    print(item)

#task2
import os
path = '/Users/kuanysspandiar/pp2-22B030287'

if os.path.exists(path):
    print(f'{path} exists')

    if os.access(path, os.R_OK):
        print(f'{path} is readable')
    else:
        print(f'{path} is not readable')

    if os.access(path, os.W_OK):
        print(f'{path} is writable')
    else:
        print(f'{path} is not writable')

    if os.access(path, os.X_OK):
        print(f'{path} is executable')
    else:
        print(f'{path} is not executable')
else:
    print(f'{path} does not exist')

#task3
import os
path = '/Users/kuanysspandiar/pp2-22B030287'

if os.path.exists(path):
    print(f'{path} exists')
       
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(f'Filename: {filename}')
    print(f'Directory: {directory}')
else:
    print(f'{path} does not exist')

#task4
file_path = '/Users/kuanysspandiar/pp2-22B030287/tsis6/lines.txt'
count = 0
with open(file_path, 'r') as file:
    for line in file:
        count+=1

print(f'The number of lines is: {count}')

#task5
file_path = '/Users/kuanysspandiar/pp2-22B030287/tsis6/lines.txt'

list1 = ['climate', 'pp2', 'world', 'python']

with open(file_path, 'w') as file:
    for word in list1:
        file.write(word + ', ')

print('COMPLETED')

#task6
for i in range(65, 91):
    letter = chr(i)
    file_name = letter + '.txt'
    with open(file_name, 'w') as file:
        file.write(f'This is file {file_name}.\n')
    print(f'File {file_name} created.')

#task7
file_path = '/Users/kuanysspandiar/pp2-22B030287/tsis6/lines.txt'
file_name = '/Users/kuanysspandiar/pp2-22B030287/tsis6/lines_copy.txt'
with open(file_path, 'r') as file,open(file_name, 'w') as file1:
    file1.write(file.read())
print('Completed succesfully')

#task8
import os
file_path = '/Users/kuanysspandiar/pp2-22B030287/tsis6/file.txt'
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    os.remove("file.txt")

