import mysql.connector as conn
import pandas as pd
import datetime
def show_books(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_book=cnx.cursor()
        cur_book.execute("select * from book order by course_id")
        temp=cur_book.fetchall()
        frame=pd.DataFrame(temp,columns=['BOOK-ID','BOOK-NAME','PRICE','AUTHOR','COURSE-ID'])
        print("Total list of books are given below")
        print(frame)
        cnx.close()
    except:
        pass
def show_status(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_book_bank=cnx.cursor()
        cur_book=cnx.cursor()
        cur_book_bank.execute("select book_id,book_amt from book_bank")
        BookBank=cur_book_bank.fetchall()
        temp=[]
        for i in BookBank:
            cur_book.execute("select book_name from book where book_id=%s",(i[0],))
            bookname=cur_book.fetchone()[0]
            a=[i[0],bookname,i[1]]
            temp.append(a)
        frame=pd.DataFrame(temp,columns=['BOOK-ID','BOOK-NAME','BOOK-AMT'])
        print(frame)
        cnx.close()
    except:
        pass
def show_borrow(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_borrow=cnx.cursor()
        cur_book=cnx.cursor()
        cur_borrow.execute("select * from borrow")
        borrow=cur_borrow.fetchall()
        temp=[]
        for i in borrow:
            cur_book.execute("select book_name from book where book_id=%s",(i[1],))
            bookname=cur_book.fetchone()[0]
            date=datetime.datetime.now()
            date1=datetime.date(date.year,date.month,date.day)
            date2=i[4]
            t=date1-date2
            if t.days>0:
                late=t.days
                fine=late*5
            else:
                late=0
                fine=0
            a=[i[0],bookname,i[2],i[4],late,fine,i[3]]
            temp.append(a)
        frame=pd.DataFrame(temp,columns=['BORROW-ID','BOOK-NAME','BORROW-DATE','RETURN-DATE','LATE','FINE','ROLL'])
        print(frame)
        cnx.close()
    except:
        pass
def show_return(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_return=cnx.cursor()
        cur_book=cnx.cursor()
        cur_return.execute("select * from return_book")
        returnbook=cur_return.fetchall()
        temp=[]
        for i in returnbook:
            cur_book.execute("select book_name from book where book_id=%s",(i[1],))
            bookname=cur_book.fetchone()[0]
            a=[i[0],bookname,i[2],i[3],i[4],i[5],i[6]]
            temp.append(a)
        frame=pd.DataFrame(temp,columns=['RETURN-ID','BOOK-NAME','DATE-BORROW','DATE-RETURN','LATE','FINE','ROLL'])
        print(frame)
        cnx.close()
    except:
        pass

