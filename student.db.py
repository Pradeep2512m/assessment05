import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("management.db")

tablelist = connection.execute("select name from sqlite_master where type='table' and name='student'").fetchall()

if tablelist != []:
    print("table already exsist")

else:
    connection.execute(''' create table student(
                       Id integer primary key autoincrement,
                       name text,
                       rollno integer,
                       admino integer,
                       examname text,
                       english integer,
                       maths integer,
                       physics integer,
                       chemistry integer,
                       biology integer

    )''')

    print("Table created")

    while True:
        print("select an option from the given menu")
        print("1. insert student data")
        print("2. view all students")
        print("3. search an student using there partial names")
        print("4. search a student using either admino or rollno")
        print("5. update the student data with admino")
        print("6. delete an student data with admino")
        print("7. display the physics topper details")
        print("8. display the total number of students in class")
        print("9. display the average mark of students scored in english")
        print("10. display the details of all students who score lessthan average marks in maths")
        print("11. display the details of above average students in chemistry")
        print("12. exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            getname = input("enter the name:")
            getrollno = input("enter the rollno:")
            getadmino = input("enter the admino:")
            getexamname = input("enter the exam name:")
            getenglish = input("enter the english mark:")
            getmaths = input("enter the maths mark:")
            getphysics = input("enter the physics mark:")
            getchemistry = input("enter the chemistry mark:")
            getbiology = input("enter the biology mark:")

            result = connection.execute(
                "insert into student(name,rollno,admino,examname,english,maths,physics,chemistry,biology) values('" + getname + "'," + getrollno + "," + getadmino + ",'" + getexamname + "'," + getenglish + "," + getmaths + "," + getphysics + "," + getchemistry + "," + getbiology + ")")

            connection.commit()

            print("data inserted successfully")

        elif choice == 2:
            result = connection.execute("select * from student")
            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 3:
            getname = input("enter the partialname to be search:")

            result = connection.execute("select * from student where name like '%" + getname + "%'")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 4:
            getrollno = input("enter the rollno to be search:")
            getadmino = input("enter the admino to be search:")

            result = connection.execute(
                "select * from student where rollno=" + getrollno + " OR admino=" + getadmino + "")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 5:
            getadmino = input("enter the admino")
            getname = input("enter the name:")
            getrollno = input("enter the rollno:")
            getexamname = input("enter the exam name:")
            getenglish = input("enter the english mark:")
            getmaths = input("enter the maths mark:")
            getphysics = input("enter the physics mark:")
            getchemistry = input("enter the chemistry mark:")
            getbiology = input("enter the biology mark:")

            result = connection.execute(
                "update student set name='" + getname + "',rollno=" + getrollno + ",examname='" + getexamname + "',english=" + getenglish + ",maths=" + getmaths + ",physics=" + getphysics + ",chemistry=" + getchemistry + ",biology=" + getbiology + " where admino=" + getadmino + "")
            connection.commit()

            print("Student data updated successfully")

            result = connection.execute("select * from student where admino=" + getadmino + "")

            print("data updated")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 6:
            getadmino = input("enter the admino: ")

            connection.execute("delete from student where admino=" + getadmino)
            connection.commit()

            print(" studentdata deleted successfully")

            result = connection.execute("select * from student")

            print("student data updated")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 7:
            result = connection.execute("select * from student where physics=(select max(physics) from student)")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)
        elif choice == 8:
            result = connection.execute("select count(*) as name from student")

            for i in result:
                print("total student count =>", i[0])

        elif choice == 9:
            result = connection.execute("select avg(english) as english from student")

            for i in result:
                print("average mark in english:", i[0])

        elif choice == 10:
            result = connection.execute("select * from student where maths<(select avg(maths) as maths from student)")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 11:
            result = connection.execute(
                "select * from student where chemistry>(select avg(chemistry) as chemistry from student)")

            table = PrettyTable(
                ["Id", "name", "rollno", "admino", "examname", "english", "maths", "physics", "chemistry", "biology"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

        elif choice == 12:
            connection.close()
            break

        else:
            print("Invalid choice")
