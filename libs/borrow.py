import mysql.connector as conn
import datetime
import sys
def borrow(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_book=cnx.cursor()
        cur_book_bank=cnx.cursor()
        cur_borrow=cnx.cursor()
        cur_course_batch_stu=cnx.cursor()
        cur_course_batch_stu.execute("select course_id from course_batch_stu where roll=%s",(roll,))
        course_id=cur_course_batch_stu.fetchone()[0]
        book=-1
        while True:
            try:
                cur_course_batch_stu.execute("select course_id from course_batch_stu where roll=%s",(roll,))
                id=cur_course_batch_stu.fetchone()[0]
                cur_book.execute("select book_name from book where course_id=%s",(id,))
                temp=cur_book.fetchall()
                count=1
                print("the books available for you.......")
                for i in temp:
                    print(count,"            ",i[0])
                    count+=1
                book=input("Enter Book name:")
                cur_book.execute("select book_id,course_id from book where book_name=%s",(book,))
                temp=cur_book.fetchone()
                bookid=temp[0]
                course=temp[1]
                b=0
                if course==course_id:
                    cur_book_bank.execute("select book_amt from book_bank where book_id=%s",(bookid,))
                    amt=cur_book_bank.fetchone()[0]
                    if amt>1:
                        b=1
                        insert_data=(
                        "INSERT INTO borrow (book_id,date_borrow,roll,date_return)"
                        "VALUES (%s,%s,%s,%s)"
                        )
                        date=datetime.datetime.now()
                        day=date.day
                        month=date.month
                        year=date.year
                        if day>25:
                            if day==26:
                                day=1
                                if month==12:
                                    year+=1
                                    month=1
                                else:
                                    month+=1
                            elif day==27:
                                day=2
                                if month==12:
                                    year+=1
                                    month=1
                                else:
                                    month+=1
                            elif day==28:
                                day=3
                                if month==12:
                                    year+=1
                                    month=1
                                else:
                                    month+=1
                            elif day==29:
                                day=4
                                if month==12:
                                    year+=1
                                    month=1
                                else:
                                    month+=1
                            elif day==30:
                                day=5
                                if month==12:
                                    year+=1
                                    month=1
                                else:
                                    month+=1
                        else:
                            day+=5
                        return_date=datetime.date(year,month,day)
                        data=(bookid,date,roll,return_date)
                        cur_borrow.execute(insert_data,data)
                        cnx.commit()
                        amt-=1
                        cur_book_bank.execute("update book_bank set book_amt=book_amt-1 where book_id=%s",(bookid,))
                        cnx.commit()
                if b==1:
                    break
                print("sorry........\n    we can't provide you this book")
                print("Enter 1 for exit \nEnter 2 for other book:",end=' ')
                a=int(input())
                if a==1:
                    cnx.close()
                    exit()
            except:
                pass
        print("successfully borrowed")
        cnx.close()
    except:
        pass

