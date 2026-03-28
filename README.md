Student Management System (Python + MySQL)

## Overview

This is a command-line based Student Management System built using Python and MySQL.
It allows users to perform CRUD operations and manage student records efficiently.

## Features

* Add new student
* View all students
* Search student (by name / ID)
* Update student details
* Delete student
* Email validation with uniqueness check
* Export student data to CSV file

---

## Tech Stack

* Python
* MySQL
* MySQL Connector (mysql-connector-python)
* CSV (for file export)

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```
pip install mysql-connector-python
```

### 3. Setup Database

* Open MySQL
* Run the `database.sql` file

### 4. Update database credentials

Edit in `main.py`:

```
host = "localhost"
user = "[your_username]"
password = "[your_password]"
database = "student_db"
```

### 5. Run the program

```
python main.py
```

---

## Export Feature

The system allows exporting all student records to a CSV file:

* File name: `students.csv`
* Automatically generated in project folder

---

## Sample Output

```
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Export Students
7. Exit
```

Written by: **Roshin Roy**

