import pymysql as mc 

connection = mc.connect(host="localhost",user="root",password="1234",database="CSProject")
cursor = connection.cursor()

def view_books():
    cursor.execute("select * from Books")
    rows = cursor.fetchall()
    if rows:
        print("\n===== |BOOKS TABLE| =====\n")
        for row in rows:
            print(row)
    else:
        print("No books found...")
        
def view_loans():
    cursor.execute("select * from BookLoan")
    rows = cursor.fetchall()
    if rows:
        print("\n===== |LOANS TABLE| =====\n")
        for row in rows:
            print(row)
    else:
        print("No loans found...")

def add_loan():
    loan_id = input("Enter Loan ID: ")
    book_id = input("Enter Book ID: ")
    member_id = input("Enter Member ID: ")
    loan_date = input("Enter Loan Date (YYYY-MM-DD): ")
    return_date = input("Enter Due Date (YYYY-MM-DD): ")
    cursor.execute("select count from Books where BookID = %s", (book_id,))
    result = cursor.fetchone()
    if not result:
        print("Book ID not found.")
        return
    quantity = result[0]
    if quantity <= 0:
        print("Book unavailable...")
        return
    cursor.execute("insert into BookLoan values(%s, %s, %s, %s, %s)", 
                   (loan_id, book_id, member_id, loan_date, return_date))
    cursor.execute("update Books set count = count - 1 where BookID = %s", (book_id,))
    connection.commit()
    print("Loan added successfully...")
    
    
def return_loan():
    loan_id = input("Enter Loan ID: ")
    cursor.execute("SELECT LoanID FROM BookLoan WHERE LoanID = %s", (loan_id,))
    loan = cursor.fetchone()
    if not loan:
        print("Loan ID is invalid..")
        return
    cursor.execute("SELECT BookID FROM BookLoan WHERE LoanID = %s", (loan_id,))
    book = cursor.fetchone()
    if book:
        cursor.execute("UPDATE Books SET count = count + 1 WHERE BookID = %s", [book])
        connection.commit()
        print("Thank you for returning the book..")

      
while True:
    print("\n====== |LIBRARY MENU| ======\n")
    print("1. View Books Table")
    print("2. View Loans Table")
    print("3. Add a Loan")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_books()
    elif choice == 2:
        view_loans()
    elif choice == 3:
        add_loan()
    elif choice == 4:
        print("Successfully Exitted...")
        break
    else:
        print("Please Try Again..")
    task = input("\nDo you wish to continue(y/n): ")
    if task == 'n' or task == 'N':
        print("Successfully Exitted...")
        break
        
cursor.close()
connection.close()