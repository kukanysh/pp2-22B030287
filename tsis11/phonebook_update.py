import psycopg2

connection = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "password", port = "5432")
cur = connection.cursor()


def create_pattern():
    global pattern
    pattern = """SELECT * FROM Phonebook
    WHERE """
    print('What type of action do you want to perform?')
    print('1)Search by part of first name')
    print('2)Search by part of last name')
    num = int(input())

    if num == 1:
        pattern+='first_name'
        print('Enter the substring of the first name:')
        substr = input()
        pattern+=" iLIKE '%{}%'".format(substr)
    
    elif num == 2:
        pattern+='last_name'
        print('Enter the substring of the last name:')
        substr = input()
        pattern+=" iLIKE '%{}%'".format(substr)

    else:
        return 'error'
    
    return pattern

def inserting(first_name, last_name, username, phone_number):
    cur.execute("SELECT count(*) FROM Phonebook WHERE first_name='{}' AND last_name='{}'".format(first_name, last_name))
    if cur.fetchone()[0]==0:
         cur.execute("""INSERT INTO Phonebook VALUES ('{}','{}', '{}', {})""".format(first_name, last_name, username, phone_number))
    else:
         cur.execute("""UPDATE Phonebook
         SET number={}
         WHERE first_name='{}' AND last_name='{}'
         """.format(phone_number,first_name, last_name))
    
def loopinsert():
    name_list = []
    while True:
        print("Want to enter a person's data? yes/no")
        mode = input()
        if mode == "no":
             break
        elif mode == "yes":
            print('Enter data...')
            person = input().split()
            if len(person)>3:
                name_list.append(person)
                continue
            
            if not person[2].isdigit():
                name_list.append(person)
                continue
            
            inserting(*person)
    
    if len(name_list) == 0:
        return
    print('You entered incorrect data format...')
    for i in name_list:
        print(i)

def pagination():
    pattern = create_pattern()
    if pattern == 'error':
        return 'error'
    print('Enter offset:')
    offset = int(input())
    pattern+=" OFFSET {}".format(offset)
    
    print("Do you need a limit?")
    answer = input()
    
    if answer == 'yes':
        print('Enter limit:')
        limit = int(input())
        pattern+=" LIMIT {}".format(limit)
    pattern +=";"

    return pattern

def delete():
    pattern="""DELETE FROM Phonebook
    WHERE """
    cur.execute("SELECT * from Phonebook")
    print(cur.fetchall())
    print('Do you want to delete?')
    mode = input()
    if mode == 'yes':
        print('Do you wanna delete by:')
        print('1) last_name')
        print('2) first_name')
        print('3) phone_number')
        num=int(input())
        if num == 1:
            print("Enter last name to delete:")
            last_name=input()
            pattern+="last_name='{}'".format(last_name)
        elif num == 2:
            print("Enter first name to delete:")
            first_name=input()
            pattern+="first_name='{}'".format(first_name)
        else:
            print("Enter phone number to delete:")
            number=input()
            pattern+="phone_number={}".format(number)
        cur.execute(pattern)
    else:
        print('error')


print('What type of action you want to perform?')
print('1)Return all records based on a pattern')
print('2)Insert new user by name and phone')
print('3)Insert many new users by list of name and phone')
print('4)Query data from the tables with pagination (by limit and offset)')
print('5)Delete data from tables by username or phone')
num = int(input())

if num == 1:
    s1 = create_pattern()
    if s1!="error":
        cur.execute(s1+";")
        print(cur.fetchall())
elif num == 2:
    first_name = input('Enter name: ')
    last_name = input('Enter surname: ')
    username = input('Enter username: ')
    phone_number = int(input('Enter phone number: '))
    inserting(first_name, last_name, username, phone_number)
elif num == 3:
    loopinsert()
elif num == 4:
    s2=pagination()
    if s2!="error":
        cur.execute(s2+";")
        print(cur.fetchall())
elif num == 5:
    delete()


connection.commit()
cur.close()
connection.close()