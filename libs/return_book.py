import mysql.connector as conn
import datetime
def return_book(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_course_batch_stu=cnx.cursor()
        cur_borrow=cnx.cursor()
        cur_book=cnx.cursor()
        cur_return_book=cnx.cursor()
        cur_return_book=cnx.cursor()
        cur_book_bank=cnx.cursor()
        book=-1
        p=0
        '''try:
            cur_borrow.execute("select book_id from borrow where roll=%s",(roll,))
            print(cur_borrow)
        except:
            pass
        show=[]
        try:
            for i in cur_borrow:
                cur_book.execute("select book_name from book where book_id=%s",(i[0],))
                fetch=cur_book.fetchone()[0]
                print(fetch)
                show.append(fetch)
        except:
            pass
        print(show)
        count=1
        print("you have borrowed........")
        for i in show:
            print(count,"          ",i)
            count+=1'''
        while True:
            book=input("name of book to return:")
            try:
                cur_borrow.execute("select book_id,date_borrow,date_return from borrow where roll=%s",(roll,))
            except:
                print("You have no books borrowed")
                cnx.close()
                exit()
            temp=cur_borrow.fetchall()
            for i in temp:
                bookid=i[0]
                cur_book.execute("select book_name from book where book_id=%s",(bookid,))
                book_name=cur_book.fetchone()[0]
                if book==book_name:
                    borrow_date=i[1]
                    return_date=i[2]
                    date=datetime.datetime.now()
                    date1=datetime.date(date.year,date.month,date.day)
                    if (date1-return_date)==0:
                        pass
                    else:
                        t=date1-return_date
                    late=t.days
                    fine=late*5
                    if fine > 0:
                        print("you have charged fine of Rs. %d"%fine)
                        while True:
                            a=int(input("Please enter payeble ammount:"))
                            if a==fine:
                                break
                            else:
                                print("please pay full ammount")
                    insert_data=(
                    "INSERT INTO return_book (book_id,date_borrow,date_return,late,fine,roll)"
                    "VALUES (%s,%s,%s,%s,%s,%s)"
                    )
                    data=(i[0],borrow_date,date,late,fine,roll)
                    cur_return_book.execute(insert_data,data)
                    cnx.commit()
                    cur_borrow.execute("delete from borrow where book_id=%s and roll=%s",(i[0],roll))
                    cnx.commit()
                    cur_book_bank.execute("update book_bank set book_amt=book_amt+1 where book_id=%s",(i[0],))
                    cnx.commit()
                    p=1
                    break
            if p==1:
                break
        print("successfully updated record")
        cnx.close()
    except:
        pass

                    
