import mysql.connector as conn
import pandas as pd
def remove_address(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_address=cnx.cursor()
        cur_address.execute("select add_id,address from address where roll=%s",(roll,))
        temp=cur_address.fetchall()
        print("the total addresses you have register are......")
        frame=pd.DataFrame(temp,columns=['address id','address'])
        print(frame)
        addid=input("Enter address id which you want to remove:")
        cur_address.execute("delete from address where add_id=%s",(addid,))
        cnx.commit()
        print("address removed successfully...?")
        cnx.close()
    except:
        pass
def remove_phone(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_phone=cnx.cursor()
        cur_phone.execute("select phone_id,phone from phone where roll=%s",(roll,))
        temp=cur_phone.fetchall()
        print("the total contacts you have register are......")
        frame=pd.DataFrame(temp,columns=['phone id','phone number'])
        print(frame)
        phoneid=input("Enter phone_id which you want to remove:")
        cur_phone.execute("delete from phone where phone_id=%s",(phoneid,))
        cnx.commit()
        print("phone number removed successfully...?")
        cnx.close()
    except:
        pass
def remove_book(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_book=cnx.cursor()
        cur_borrow=cnx.cursor()
        cur_book_bank=cnx.cursor()
        cur_student=cnx.cursor()
        cur_book.execute("select book_id,book_name from book")
        temp=cur_book.fetchall()
        frame=pd.DataFrame(temp,columns=['BOOK-ID','BOOK-NAME'])
        print("total books we have......")
        print(frame)
        bookid=int(input("Enter the book-id for which book you want to remove:"))
        try:
            cur_borrow.execute("select roll from borrow where book_id=%s",(bookid,))
            rolls=[]
            stu=[]
            for i in cur_borrow:
                rolls.append(i[0])
            if len(rolls)==0:
                raise ValueError()
            print("You cannot remove this book.......\nsome peoples have borrowed this book")
            print("the peoples are.........")
            for i in rolls:
                cur_student.execute("select roll,f_name,l_name from student where roll=%s",(i,))
                temp=cur_student.fetchone()
                stu.append(temp)
            frame2=pd.DataFrame(stu,columns=['ROLL','FNAME','LNAME'])
            print(frame2)
            cnx.close()
        except:
            cur_book_bank.execute("delete from book_bank where book_id=%s",(bookid,))
            cnx.commit()
            cur_book.execute("delete from book where book_id=%s",(bookid,))
            cnx.commit()
            print("book removed successfully from the record.....")
            cnx.close()
    except:
        pass
def remove_student(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_book=cnx.cursor()
        cur_borrow=cnx.cursor()
        cur_phone=cnx.cursor()
        cur_address=cnx.cursor()
        cur_course_batch_stu=cnx.cursor()
        cur_login=cnx.cursor()
        cur_student=cnx.cursor()
        cur_student.execute("select roll,f_name,l_name from student")
        temp=cur_student.fetchall()
        frame=pd.DataFrame(temp,columns=['ROLL','F-NAME','L-NAME'])
        print("total students we have......")
        print(frame)
        user=int(input("Enter the roll number for which student you want to remove:"))
        try:
            cur_borrow.execute("select book_id from borrow where roll=%s",(user,))
            bookids=[]
            books=[]
            for i in cur_borrow:
                bookids.append(i[0])
            if len(bookids)==0:
                raise ValueError()
            print("You cannot remove the student.......\nthis student has borrowed some books")
            print("the books are.........")
            for i in bookids:
                cur_book.execute("select book_id,book_name from book where book_id=%s",(i,))
                temp=cur_book.fetchone()
                books.append(temp)
            frame2=pd.DataFrame(books,columns=['BOOK-ID','NAME'])
            print(frame2)
            cnx.close()
        except:
            cur_phone.execute("delete from phone where roll=%s",(user,))
            cnx.commit()
            cur_address.execute("delete from address where roll=%s",(user,))
            cnx.commit()
            cur_course_batch_stu.execute("delete from course_batch_stu where roll=%s",(user,))
            cnx.commit()
            cur_login.execute("delete from login where roll=%s",(user,))
            cnx.commit()
            cur_student.execute("delete from student where roll=%s",(user,))
            cnx.commit()
            print("student removed  successfully from the record.....")
            cnx.close()
    except:
        pass





