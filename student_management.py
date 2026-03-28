import mysql.connector

host = "localhost"
port = 3306
user = ""
password = ""
database = "student_db"

connection = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

class Student:
    def __init__(self, name, age, course, email):
        self.name = name
        self.age = age
        self.course = course
        self.email = email


def is_valid_email(email):
    if "@" in email and email.endswith(".com"):
        return True
    return False

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    
    while True:
        email = input("Enter email: ")
        if is_valid_email(email):
            cursor.execute(
                "SELECT * FROM students WHERE email = %s", (email,)
            )
            rows = cursor.fetchall()
            if len(rows) == 0:
                break
            else:
                print("This email already exists. Please use another email.")
        else:
            print("Invalid email! Must contain '@' and end with '.com'")

    s = Student(name, age, course, email)
    
    try:
        cursor.execute("INSERT INTO students (name, age, course, email) VALUES (%s, %s, %s, %s)",
            (s.name, s.age, s.course, s.email))
        connection.commit()
        print("Student added successful")
    except mysql.connector.IntegrityError as e:
        print("This email already exists. Please use another email.",e)
        return

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No students found")


def search_student():
    choice = input("1. Search by name\n2. Search by Id\nEnter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
    elif choice == "2":
        id = int(input("Enter student id: "))
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    else:
        print("Invalid choice")
        return
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No student found")


def update_student():
    id = int(input("Enter student id: "))
    
    choice = input("1. Update name\n2. Update age\n3. Update course\n4. Update email\n5. Update all\n6.exit\nEnter your choice: ")
    
    if choice == "1":
        name = input("Enter new name: ")
        cursor.execute("UPDATE students SET name = %s WHERE id = %s", (name, id))
    elif choice == "2":
        age = int(input("Enter new age: "))
        cursor.execute("UPDATE students SET age = %s WHERE id = %s", (age, id))
    elif choice == "3":
        course = input("Enter new course: ")
        cursor.execute("UPDATE students SET course = %s WHERE id = %s", (course, id))
    elif choice == "4":
        while True:
            email = input("Enter new email: ")
            if is_valid_email(email):
                break
            else:
                print("Invalid email!")
    
        try:
            cursor.execute("UPDATE students SET email = %s WHERE id = %s", (email, id))
            connection.commit()
            print("Updation successful")
        except mysql.connector.IntegrityError as e:
            print("This email already exists. Please use another email.",e)
            return
    
    elif choice == "5":
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
    
        while True:
            email = input("Enter new email: ")
            if is_valid_email(email):
                break
            else:
                print("Invalid email!")
                
        try:
            cursor.execute("UPDATE students SET name = %s, age = %s, course = %s, email = %s WHERE id = %s",(name, age, course, email, id))
            connection.commit()
            print("Updation successful")
        except mysql.connector.IntegrityError as e:
            print("This email already exists. Please use another email.",e)
            return
        
    elif choice == "6":
        print("Exiting updation")
        return
    
    else:
        print("Invalid choice")
        return
    

    connection.commit()
    print("Updation successful")


def delete_student():
    id = int(input("Enter student id: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    connection.commit()
    print("Deletion successful")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program")
        break
    else:
        print("Invalid choice")


cursor.close()
connection.close()
