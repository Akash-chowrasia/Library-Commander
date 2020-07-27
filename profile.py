import mysql.connector as conn
import pandas as pd
import datetime
def helpadmin():
    print(""" <<<<<<<<<<<<ADMIN COMMAND HELP PAGE>>>>>>>>>>>>>
================================================
================================================
1) ADD BOOKS -- add book username password
2) UPDATE --:
    (a)... update bookammount username password
    (b)... update password username password
3) REMOVE --:
    (a)... remove book username password
    (b)... remove student username password
4) SHOW --:
    (a)... show books username password
    (b)... show librarystatus username password
    (c)... show borrowlist username password
    (d)... show returnlist username password
    (e)... show profile username password
5) HELP -- help username password            """)
def helpstudent():
    print(""" <<<<<<<<<<<<STUDENTS COMMAND HELP PAGE>>>>>>>>>>>>>
==========================================================
==========================================================
1) ADD --:
    (a)... add phone username password
    (b)... add address username password
2) UPDATE --:
    (a)... update email username password
    (b)... update phone username password
    (c)... update address username password
    (d)... update password username password
3) REMOVE --:
    (a)... remove phone username password
    (b)... remove address username password
4) BORROW -- borrow username password
5) RETURNBOOK -- returnbook username password
6) PROFILE -- show profile username password
7) HELP -- help username password            """)
def show_profile_student(x):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_student=cnx.cursor()
        cur_book=cnx.cursor()
        cur_phone=cnx.cursor()
        cur_address=cnx.cursor()
        cur_borrow=cnx.cursor()
        cur_course=cnx.cursor()
        cur_batch=cnx.cursor()
        cur_course_batch_stu=cnx.cursor()
        cur_login=cnx.cursor()
        cur_return_book=cnx.cursor()
        cur_borrow1=cnx.cursor()
        cur_student.execute("select * from student where roll=%s",(x,))
        student=cur_student.fetchall()
        cur_course_batch_stu.execute("select * from course_batch_stu where roll=%s",(x,))
        course_batch_stu=cur_course_batch_stu.fetchall()
        cur_phone.execute("select * from phone where roll=%s",(x,))
        phone=cur_phone.fetchall()
        cur_address.execute("select * from address where roll=%s",(x,))
        address=cur_address.fetchall()
        cur_course.execute("select * from course where course_id=%s",(course_batch_stu[0][0],))
        course=cur_course.fetchall()
        cur_batch.execute("select * from batch where batch_id=%s",(course_batch_stu[0][1],))
        batch=cur_batch.fetchall()
        cur_login.execute("select * from login where roll=%s",(x,))
        login=cur_login.fetchall()
        print("---:PERSONAL DETAILS:---")
        print("Roll number:",x)
        print("Name:",student[0][1],student[0][2])
        print("Phone number:")
        for i in phone:
            print(i[1])
        print("Email:",student[0][3])
        print("Address:")
        for i in address:
            print(i[1])
        print("\n---:ACADEMIC DETAILS:---")
        print("Batch Id:",batch[0][0])
        print("Course Id:",course[0][0])
        print("Course Name:",course[0][1])
        print("Start Year:",batch[0][1])
        print("End year:",batch[0][2])
        cur_borrow.execute("select * from borrow where roll=%s",(x,))
        borrow=cur_borrow.fetchall()
        cur_return_book.execute("select * from return_book where roll=%s",(x,))
        return_book=cur_return_book.fetchall()
        cur_book.execute("select book_name from book where book_id=%s",(borrow[0][1],))
        book=cur_book.fetchall()
        cur_borrow1.execute("select book_id,date_borrow,date_return from borrow where roll=%s",(x,))
        borrow1=cur_borrow1.fetchall()

        print("---:Library Details:---")
        l=[]
        for i in borrow1:
            a=list(i)
            l.append(a)
        for i in range(len(l)):
            date=datetime.datetime.now()
            date1=datetime.date(date.year,date.month,date.day)
            date2=borrow[i][4]
            t=date1-date2
            if t.days>0:
                late=t.days
                fine=late*5
                l[i].append(late)
                l[i].append(fine)
            else:
                l[i].append(0)
                l[i].append(0)
        temp=pd.DataFrame(l,columns=['BOOK-ID','BORROW-DATE','RETURN-DATE','LATE','FINE'])
        print(temp)
        cnx.close()
    except:
        pass

def show_profile_admin():
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_student=cnx.cursor()
        print("---:PROFILE PAGE:---")
        cur_student.execute("select * from student")
        student=cur_student.fetchall()
        print("Roll        Name")
        for i in student:
            if i[0] != 1010101:
                print(i[0],"   ",i[1],i[2])
        x=int(input("please select a roll number to see profile:"))
        show_profile_student(x)
        cnx.close()
    except:
        pass

