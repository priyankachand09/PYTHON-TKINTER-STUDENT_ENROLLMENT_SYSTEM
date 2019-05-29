import sqlite3  # sqlite library #database


connection = sqlite3.connect('student.db')
print("DATABASE OPENED SUCCESSFULLY")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_adddress"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                   + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, "+ STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE +
                   " INTEGER);")
print("table created successfully")

## insert new record

def insert_record(name, college, address, phone):

    connection.execute("INSERT INTO " + TABLE_NAME + " ( "
                       + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " +
                       STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + name + "', '" + college +
                       "', '" + address + "', " +
                       str(phone) + " ); ")
    connection.commit()
    print("Data saved successfully.")

def display_records():

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME)

    for row in cursor:
        print("Student id is: ", row[0])
        print("Student name is: ", row[1])
        print("Student college is: ", row[2])

    connection.close()