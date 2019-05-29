import tkinter as tk
from tkinter import messagebox
from Modules import data as dt
mainWindow = tk.Tk()
mainWindow.title("student_enrollment_sysytem")


la = tk.Label(mainWindow,text="STUDENT_ENROLLMENT_SYSTEM", pady=50, padx=20)
la.pack()


l1 = tk.Label(mainWindow,text="STUDENT NAME", pady=10, padx=20)
l1.pack()

Student_Name = tk.Entry(mainWindow,textvar='textin')
Student_Name.pack(padx=0,pady=0)

l2 = tk.Label(mainWindow, text="STUDENT COLLEGE", pady=10, padx=20)
l2.pack()

Student_College = tk.Entry(mainWindow)
Student_College.pack()

l3 = tk.Label(mainWindow, text="STUDENT ADDRESS", pady=10, padx=20)
l3.pack()

Student_Address = tk.Entry(mainWindow)
Student_Address.pack()

l4 = tk.Label(mainWindow, text="PHONE", pady=10, padx=20)
l4.pack()

Student_Phone = tk.Entry(mainWindow)
Student_Phone.pack()

def takeValueInput():
    name = Student_Name.get()
    college = Student_College.get()
    address = Student_Address.get()
    phone = int(Student_Phone.get())

    dt.insert_record(name, college, address, phone)


save_button = tk.Button(mainWindow, text='SAVE',
                        command = lambda : takeValueInput())
save_button.pack()

display_button = tk.Button(mainWindow, text='DISPLAY', command = lambda : dt.display_records())
display_button.pack()


mainWindow.mainloop()