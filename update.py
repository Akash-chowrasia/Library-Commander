import mysql.connector as conn
import pandas as pd
def update_email(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_email=cnx.cursor()
        newmail=input("NEW E-MAIL:")
        cur_email.execute("update student set email=%s where roll=%s",(newmail,roll))
        cnx.commit()
        print("E-mail updated successfully...?")
        cnx.close()
    except:
        pass
def update_phone(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_phone=cnx.cursor()
        cur_phone.execute("select phone_id,phone from phone where roll=%s",(roll,))
        temp=cur_phone.fetchall()
        print("the total contacts you have register are......")
        frame=pd.DataFrame(temp,columns=['phone id','phone number'])
        print(frame)
        phoneid=input("Enter phone_id which you want to update:")
        phone=input("Enter new phone number:")
        cur_phone.execute("update phone set phone=%s where phone_id=%s",(phone,phoneid))
        cnx.commit()
        print("phone number updated successfully...?")
        cnx.close()
    except:
        pass
def update_address(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_address=cnx.cursor()
        cur_address.execute("select add_id,address from address where roll=%s",(roll,))
        temp=cur_address.fetchall()
        print("the total addresses you have register are......")
        frame=pd.DataFrame(temp,columns=['address id','address'])
        print(frame)
        addid=input("Enter address id which you want to update:")
        address=input("Enter new address number:")
        cur_address.execute("update address set address=%s where add_id=%s",(address,addid))
        cnx.commit()
        print("address updated successfully...?")
        cnx.close()
    except:
        pass
def update_bookammount(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_book=cnx.cursor()
        cur_book_bank=cnx.cursor()
        cur_book.execute("select book_id,book_name from book")
        temp=cur_book.fetchall()
        list=[]
        print("Total books in library....")
        #print("BOOK-ID          BOOK-AMT          BOOK-NAME")
        for i in temp:
            cur_book_bank.execute("select book_amt from book_bank where book_id=%s",(i[0],))
            temp1=cur_book_bank.fetchone()[0]
            list.append([i[0],temp1,i[1]])
            #print("%d          %d            %s"%(i[0],temp1,i[1]))
        frame=pd.DataFrame(list,columns=['BOOK-ID','BOOK-AMT','BOOK-NAME'])
        print(frame)
        book=input("Enter the book id for which you have to  change the book ammount:")
        ammount=input("Enter new book ammount:")
        cur_book_bank.execute("update book_bank set book_amt=%s where book_id=%s",(ammount,book))
        cnx.commit()
        cnx.close()
    except:
        pass

def update_password(roll,password):
    try:
        cnx=conn.connect(user='root',password='swapn',host='127.0.0.1',database='library')
        cur_login=cnx.cursor()
        x=input("please enter new password you want to set")
        cur_login.execute("update login set password=%s where roll=%s",(x,roll))
        cnx.commit()
        print("password updated successfully")
        cnx.close()
    except:
        pass
