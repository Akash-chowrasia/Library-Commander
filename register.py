import mysql.connector as conn
def register():
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_student=cnx.cursor()
        cur_phone=cnx.cursor()
        cur_address=cnx.cursor()
        cur_course=cnx.cursor()
        cur_batch=cnx.cursor()
        cur_course_batch_stu=cnx.cursor()
        cur_login=cnx.cursor()
        fname=input("FIRST NAME:")
        lname=input("LAST NAME:")
        while True:
            email=input("E-MAIL:")
            e=email.lower()
            if e.endswith("@gmail.com") or e.endswith("@yahoo.com") or e.endswith("@linuxmail.com") or e.endswith("@mail.com"):
                break
            else:
                print("..............input a valid email?")
        while True:
            phone=int(input("PHONE:"))
            p=str(phone)
            if len(p)==10:
                break
            else:
                print("..............input a valid contact")
        address=input("ADDRESS:")
        course=-1
        course_id=-1
        p=0
        cur_course.execute("select * from course")
        while True:
            course=input("COURSE:")
            for i in cur_course:
                if i[1]==course:
                    course_id=i[0]
                    p=1
            else:
                if p==0:
                    print("sorry.......\n        this course is not available")
            if p==1:
                break
        batch=-1
        p=0
        cur_batch.execute("select * from batch")
        while True:
            batch=int(input("BATCH:"))
            for i in cur_batch:
                if i[0]==batch:
                    p=1
            else:
                if p==0:
                    print("sorry.......\n        invalid batch number")
            if p==1:
                break
        password='123'
        while True:
            password=input("PASSWORD:")
            password_confirm=input("CONFIRM PASSWORD:")
            if password==password_confirm:
                break
            print("password should be same")
        insert_data = (
        "INSERT INTO student (f_name,l_name,email) "
        "VALUES (%s, %s, %s)"
        )
        data=(fname,lname,email)
        cur_student.execute(insert_data,data)
        cnx.commit()
        cur_student.execute("select roll from student where f_name=%s and l_name=%s and email=%s",(fname,lname,email))
        roll=cur_student.fetchone()[0]
        insert_data=(
        "INSERT INTO phone (phone,roll)"
        "VALUES (%s,%s)"
        )
        data=(phone,roll)
        cur_phone.execute(insert_data,data)
        cnx.commit()
        insert_data=(
        "INSERT INTO address (address,roll)"
        "VALUES (%s,%s)"
        )
        data=(address,roll)
        cur_address.execute(insert_data,data)
        cnx.commit()
        insert_data=(
        "INSERT INTO course_batch_stu (course_id,batch_id,roll)"
        "VALUES (%s,%s,%s)"
        )
        data=(course_id,batch,roll)
        cur_course_batch_stu.execute(insert_data,data)
        cnx.commit()
        insert_data=(
        "INSERT INTO login (roll,password)"
        "VALUES (%s,%s)"
        )
        data=(roll,password)
        cur_login.execute(insert_data,data)
        cnx.commit()
        print("Congratulations..........\n You have successfully registered")
        print("your username=",roll)
        cnx.close()
    except:
        pass



