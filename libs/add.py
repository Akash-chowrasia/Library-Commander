import mysql.connector as conn
def add_phone(roll,password):
    cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
    cur_phone=cnx.cursor()
    phn=input("Enter phone:")
    insert_data=(
    "INSERT INTO phone (phone,roll)"
    "VALUES (%s,%s)"
    )
    data=(phn,roll)
    cur_phone.execute(insert_data,data)
    cnx.commit()
    print("phone number added successfully")
    cnx.close()
def add_address(roll,password):
    cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
    cur_address=cnx.cursor()
    add=input("Enter address:")
    insert_data=(
    "INSERT INTO address (address,roll)"
    "VALUES (%s,%s)"
    )
    data=(add,roll)
    cur_address.execute(insert_data,data)
    cnx.commit()
    print("address added successfully")
    cnx.close()
def add_book(roll,password):
    cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
    cur_book=cnx.cursor()
    cur_course=cnx.cursor()
    cur_book_bank=cnx.cursor()
    book=input("Enter book name:")
    price=int(input("Price:"))
    author=input("Auther:")
    while True:
        course=input("Course:")
        try:
            cur_course.execute("select course_id from course where course_name=%s",(course,))
            courseid=cur_course.fetchone()[0]
            break
        except:
            print("This course is not present.....?")
            print("Enter 1 for enter new course \nor, Enter 2 for exit")
            a=input("Enter:")
            if a==2:
                exit()
    book_ammount=int(input("Number of books:"))
    insert_data=(
    "INSERT INTO book (book_name,price,author,course_id)"
    "VALUES (%s,%s,%s,%s)"
    )
    data=(book,price,author,courseid)
    cur_book.execute(insert_data,data)
    cnx.commit()
    cur_book.execute("select book_id from book where course_id=%s and book_name=%s and author=%s",(courseid,book,author))
    bookid=cur_book.fetchone()[0]
    insert_data1=(
    "INSERT INTO book_bank (course_id,book_id,book_amt)"
    "VALUES (%s,%s,%s)"
    )
    data1=(courseid,bookid,book_ammount)
    cur_book_bank.execute(insert_data1,data1)
    cnx.commit()
    print("book details added successfully")
    cnx.close()
