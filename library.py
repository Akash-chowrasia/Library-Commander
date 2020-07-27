import sys
import os
sys.path.append('/libs/')
import libs
sys.path.append('/color/')
import color
from color.ColorPython import Color
from libs.register import *
from libs.borrow import *
from libs.return_book import *
from libs.update import *
from libs.add import *
from libs.remove import *
from libs.librarybase import *
from libs.profile import *
import mysql.connector as conn
from sys import argv
os.system("cls")
print( Color.bold['green'] + "*"*os.get_terminal_size()[0] + Color.reset)
print("                                   "+ Color.bold['purple']+"--WELCOME TO LIBRARY MANAGEMENT SYSTEM--"+Color.reset)
print( Color.bold['green'] + "*"*os.get_terminal_size()[0] + Color.reset)
cnx=conn.connect(user='root',password='Aa@9830367895',host='127.0.0.1',database='library')
try:
    if argv[1].lower()=='register':
        register()
    elif argv[1].lower()=='borrow':
        cur_login=cnx.cursor()
        cur_admin=cnx.cursor()
        try:
            cur_admin.execute("select password from login where roll=1010101")
            admin=cur_admin.fetchone()[0]
            cur_login.execute("select password from login where roll=%s",(int(argv[2]),))
            password=cur_login.fetchone()[0]
            if password==argv[3]:
                if password==admin:
                    print( Color.bold['red']+"sorry .....\n          admines does not borrow or return books" +Color.reset)
                else:
                    borrow(int(argv[2]),argv[3])
            else:
                print( Color.bold['red']+"Access denied...\n      Password is wrong"+Color.reset)
        except:
            print(Color.bold['red']+"\n\n        ........User not exist"+Color.reset)
    elif argv[1].lower()=='returnbook':
        cur_login=cnx.cursor()
        cur_admin=cnx.cursor()
        try:
            cur_admin.execute("select password from login where roll=1010101")
            admin=cur_admin.fetchone()[0]
            cur_login.execute("select password from login where roll=%s",(int(argv[2]),))
            password=cur_login.fetchone()[0]
            if password==argv[3]:
                if password==admin:
                    print( Color.bold['red']+"sorry .....\n          admines does not borrow or return books" +Color.reset)
                else:
                    return_book(int(argv[2]),argv[3])
            else:
                print(Color.bold['red']+"Access denied...\n      Password is wrong"+Color.reset)
        except:
            print(Color.bold['red']+"\n\n          .......User not exist"+Color.reset)
    elif argv[1].lower()=='help':
        cur_login=cnx.cursor()
        cur_admin=cnx.cursor()
        try:
            cur_admin.execute("select password from login where roll=1010101")
            admin=cur_admin.fetchone()[0]
            cur_login.execute("select password from login where roll=%s",(int(argv[2]),))
            password=cur_login.fetchone()[0]
            if password==argv[3]:
                if password==admin:
                    helpadmin()
                else:
                    helpstudent()
            else:
                print(Color.bold['red']+"Access denied...\n      Password is wrong"+Color.reset)
        except:
            print(Color.bold['red']+"User not exist"+Color.reset)
    elif argv[1].lower()=='add':
        if argv[2].lower()=='phone':
            cur_login=cnx.cursor()
            cur_admin=cnx.cursor()
            try:
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"this section is for student use only\n         you dont have phone section"+Color.reset)
                    else:
                        add_phone(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied...\n      Password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='address':
            cur_login=cnx.cursor()
            cur_admin=cnx.cursor()
            try:
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"this section is for student use only \n          you don't have address section"+Color.reset)
                    else:
                        add_address(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied...\n      Password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='book':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        add_book(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n          Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied...\n      Password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)

    elif argv[1].lower()=='update':
        if argv[2].lower()=='email':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"you dont have email record to update"+Color.reset)
                    else:
                        update_email(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='phone':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"you dont have any phone number record"+Color.reset)
                    else:
                        update_phone(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='address':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"you dont have address record"+Color.reset)
                    else:
                        update_address(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='bookammount':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        update_bookammount(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n        Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['res']+"User not exist"+Color.reset)
        elif argv[2].lower()=='password':
            cur_login=cnx.cursor()
            try:
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    update_password(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
    elif argv[1].lower()=='remove':
        if argv[2].lower()=='phone':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"you dont have any phone number"+Color.reset)
                    else:
                        remove_phone(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='address':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        print(Color.bold['red']+"you dont have any address record"+Color.reset)
                    else:
                        remove_address(int(argv[3]),argv[4])
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='book':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        remove_book(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n            Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        elif argv[2].lower()=='student':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        remove_student(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n            Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
    elif argv[1].lower()=='show':
        if argv[2].lower()=='books':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        show_books(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n            Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        if argv[2].lower()=='librarystatus':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        show_status(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n            Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        if argv[2].lower()=='borrowlist':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        show_borrow(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n            Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        if argv[2].lower()=='returnlist':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        show_return(int(argv[3]),argv[4])
                    else:
                        print(Color.bold['red']+"sorry......\n            Authentication failed"+Color.reset)
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)
        if argv[2].lower()=='profile' or argv[2].lower()=='profiles':
            cur_login=cnx.cursor()
            try:
                cur_admin=cnx.cursor()
                cur_admin.execute("select password from login where roll=1010101")
                admin=cur_admin.fetchone()[0]
                cur_login.execute("select password from login where roll=%s",(int(argv[3]),))
                password=cur_login.fetchone()[0]
                if password==argv[4]:
                    if password==admin:
                        show_profile_admin()
                    else:
                        show_profile_student(int(argv[3]))
                else:
                    print(Color.bold['red']+"Access denied....\n     password is wrong"+Color.reset)
            except:
                print(Color.bold['red']+"User not exist"+Color.reset)

    cnx.close()
except:
    pass
            

