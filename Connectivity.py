import pymysql as mc
import sys

connection = mc.connect(host="localhost",user="root",password="1234",database="CSProject")
cursor = connection.cursor()
task_option=['y','n','Y','N']

def view_books():
    cursor.execute("select * from Books")
    rows = cursor.fetchall()
    if rows:
        print("\n===== |BOOKS TABLE| =====\n")
        for row in rows:
            print(row)
    else:
        print("No books found...")
    task = input("\nDo you wish to continue(Y/N): ")
    x=1
    while x==1:
     if task in task_option:
        if task.lower()=='y':
         task_TODO()
        else:
         print("Successfully Exitted Program...")
         sys.exit()
     else:
        print("Given Input Undefined...")
        task = input("Do you wish to continue(Y/N): ")
        x=1

def view_loans():
    cursor.execute("select * from BookLoan")
    rows = cursor.fetchall()
    if rows:
        print("\n===== |LOANS TABLE| =====\n")
        for row in rows:
            print(row)
    else:
        print("No loans found...")
    task = input("\nDo you wish to continue(Y/N): ")
    x=1
    while x==1:
     if task in task_option:
        if task.lower()=='y':
         task_TODO()
        else:
         print("Successfully Exitted Program...")
         sys.exit()
     else:
        print("Given Input Undefined...")
        task = input("Do you wish to continue(Y/N): ")
        x=1


def add_loan():
    loan_id = input("Enter Loan ID: ")
    book_id = input("Enter Book ID: ")
    member_id = input("Enter Member ID: ")
    loan_date = input("Enter Loan Date (YYYY-MM-DD): ")
    return_date = input("Enter Due Date (YYYY-MM-DD): ")
    cursor.execute("insert into BookLoan values(%s, %s, %s, %s, %s)", (loan_id, book_id, member_id, loan_date, return_date))
    connection.commit()
    print("Loan added successfully!")
    task = input("\nDo you wish to continue(Y/N): ")
    x=1
    while x==1:
     if task in task_option:
        if task.lower()=='y':
         task_TODO()
        else:
         print("Successfully Exitted Program...")
         sys.exit()
     else:
        print("Given Input Undefined...")
        task = input("Do you wish to continue(Y/N): ")
        x=1
    

def task_TODO():
 choice = 1
 while choice <=4:
    print("\n====== |LIBRARY MENU| ======\n")
    print("1. View Books Table")
    print("2. View Loans Table")
    print("3. Add a Loan")
    print("4. Exit")
    choice = int(input("\nChoose an option: "))
    if choice == 1:
        view_books()
    elif choice == 2:
        view_loans()
    elif choice == 3:
        add_loan()
    elif choice == 4:
        print("Successfully Exitted Program...")
        sys.exit()
    else:
        print("\nGiven Option Undefined...")
        print("Please Try Again...")
        choice = 1

    
task_TODO()
cursor.close()
connection.close()