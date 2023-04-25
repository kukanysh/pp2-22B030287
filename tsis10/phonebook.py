import psycopg2

print("===========================================")
print("What type of action do you want to execute?")
print("1) UPLOAD DATA FROM CSV FILE")
print("2) UPLOAD DATA FROM CONSOLE")
num = int(input())
connection = psycopg2.connect(
    host = "localhost",
    database = "phonebook",
    user = "postgres",
    password = "password"
)

cursor = connection.cursor()

# if num == 1:
#     COPY users(username, first_name, last_name, phone_number) FROM 'path' WITH (FORMAT csv, HEADER);
           
# elif num == 2:

connection.commit()
cursor.close()
connection.close()