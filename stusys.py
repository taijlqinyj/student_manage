# @DESCRIPTION: 
# @AUTHOR : qindarke
# @DATE : 2024/5/20 10:09
import os


def menu():
    print("Student Info Management System".center(60, "="))
    print("Function Menu".center(60, "-"))
    print("\t\t\t\t1. Create Student Information".ljust(60, " "))
    print("\t\t\t\t2. Select Student Information".ljust(60, " "))
    print("\t\t\t\t3. Delete Student Information".ljust(60, " "))
    print("\t\t\t\t4. Modify Student Information".ljust(60, " "))
    print("\t\t\t\t5. Sort Student's Score".ljust(60, " "))
    print("\t\t\t\t6. Count Student Total".ljust(60, " "))
    print("\t\t\t\t7. Display All Student Information".ljust(60, " "))
    print("\t\t\t\t0. Exist This System".ljust(60, " "))
    print("".center(60, "-"))


def main():
    while True:
        menu()
        choice = 11
        try:
            choice = int(input("Please input 0 ~ 7 : "))
        except:
            print("Please input integers around 0 ~ 7")
        if choice in range(0, 8):
            if choice == 0:  # exist system
                aw = input("Are you sure to exist system ? (y / n) : ")
                if aw == "y" or aw == "Y":
                    print("Thanks for your coming! Bye Bye......")
                    break
                if aw == "n" or aw == "N":
                    continue
            if choice == 1:  # create
                createStu()
            if choice == 2:  # select
                selectStu()
            if choice == 3:  # delete
                deleteStu()
            if choice == 4:  # modify
                modifyStu()
            if choice == 5:  # sort
                sortStu()
            if choice == 6:  # count
                countStu()
            if choice == 7:  # display
                displayStu()


def createStu():
    stu_list = []
    while True:
        id = input("Enter ID : ".ljust(30, " "))
        if not id:
            break
        name = input("Enter Name : ".ljust(30, " "))
        if not name:
            break
        try:
            english_score = int(input("Enter English Score : ".ljust(30, " ")))
            python_score = int(input("Enter Python Score : ".ljust(30, " ")))
            java_score = int(input("Enter Java Score : ".ljust(30, " ")))
        except:
            print("Please enter right content, try again!!!")
            continue
        stu_dir = {"id": id, "name": name, "english": english_score, "python": python_score, "java": java_score}
        stu_list.append(stu_dir)
        aw = input("Do you want to create again ? (y / n) : ")
        if aw == "y" or aw == "Y":
            continue
        else:
            break
    saveStu(stu_list)
    print("That's All !")


def saveStu(stu_list):
    try:
        stu_file = open("students.txt", "a", encoding="utf-8")
    except:
        stu_file = open("students.txt", "w", encoding="utf-8")
    for stu in stu_list:
        stu_file.write(str(stu) + "\n")
    stu_file.close()


def selectStu():
    while True:
        if os.path.exists("students.txt"):
            res = []
            with open("students.txt", "r", encoding="utf-8") as stu_file:
                stu = stu_file.readlines()
            select = int(input("If you want to query by id enter 1, query by name enter 2, end query enter 0 : "))
            if stu:
                if select == 0:
                    break
                elif select == 1:
                    query = input("Please enter student's id : ")
                    for item in stu:
                        dit = dict(eval(item))
                        if dit["id"] == query:
                            res.append(dit)
                elif select == 2:
                    query = input("Please enter student's name : ")
                    for item in stu:
                        dit = dict(eval(item))
                        if dit["name"] == query:
                            res.append(dit)
                else:
                    print("Please enter right content, try again!!!")

            if res:
                format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t"
                print(format_title.format("id", "name", "english", "python", "java", "total"))
                for stu in res:
                    total = int(stu["english"]) + int(stu["python"]) + int(stu["java"])
                    print(
                        format_title.format(stu["id"], stu["name"], stu["english"], stu["python"], stu["java"], total))
            else:
                print("No student information available")
        else:
            print("No student information available")
            break


def deleteStu():
    while True:
        stu_id = input("Please enter student id to delete : ")
        if stu_id:
            if os.path.exists("students.txt"):
                with open("students.txt", "r", encoding="utf-8") as stu_file:
                    stu_old = stu_file.readlines()
            else:
                stu_old = []
            flag = False  # 标记是否删除
            if stu_old:
                with open("students.txt", "w", encoding="utf-8") as student:
                    dit = {}
                    for item in stu_old:
                        dit = dict(eval(item))
                        if dit["id"] != stu_id:
                            student.write(str(dit) + "\n")
                        else:
                            flag = True
                    if flag:
                        print("It's already deleted which student id is {0}".format(stu_id))
                    else:
                        print("Can not found which student id is {0}".format(stu_id))
            else:
                print("No student information available")
                break
            selectStu()
            aw = input("Do you want to delete info again ? (y / n)")
            if aw == "Y" or aw == "y":
                continue
            else:
                break


def modifyStu():
    displayStu()
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as rfile:
            stu_info = rfile.readlines()
    else:
        return
    stu_id = input("Please enter student id to modify : ")
    # 判断信息是否存在
    if stu_info:
        with open("students.txt", "w", encoding="utf-8") as student:
            for item in stu_info:
                dit = dict(eval(item))
                if dit["id"] == stu_id:
                    while True:
                        try:
                            dit["name"] = input("Enter Name : ".ljust(30, " "))
                            dit["english"] = int(input("Enter English Score : ".ljust(30, " ")))
                            dit["python"] = int(input("Enter Python Score : ".ljust(30, " ")))
                            dit["java"] = int(input("Enter Java Score : ".ljust(30, " ")))
                        except:
                            print("Please enter right content, try again!!!")
                            continue
                        else:
                            break
                    student.write(str(dit) + "\n")
                    print("Modify student info successes")
                else:
                    student.write(str(dit) + "\n")
        aw = input("Do you want to modify info again ? (y / n)")
        if aw == "Y" or aw == "y":
            modifyStu()
    else:
        print("No student information available")


def sortStu():
    displayStu()
    su_dict = []
    asc_or_desc_bool = False
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as read:
            readStu = read.readlines()
        for item in readStu:
            stuDict = dict(eval(item))
            su_dict.append(stuDict)
    else:
        print("No student information available")

    asc_or_desc = int(input("Please choice asc or desc (0 is asc, 1 is desc) : "))
    if asc_or_desc == 0:
        asc_or_desc_bool = False
    elif asc_or_desc == 1:
        asc_or_desc_bool = True
    else:
        print("Please enter right content, try again")
        sortStu()
    mode = int(input(
        "Please choice sort order (1 sorted by english, 2 sorted by python, 3 sorted by java, 0 sorted by total) : "))
    if mode == 1:
        su_dict.sort(key=lambda x: int(x.get("english")), reverse=asc_or_desc_bool)
    elif mode == 2:
        su_dict.sort(key=lambda x: int(x.get("python")), reverse=asc_or_desc_bool)
    elif mode == 3:
        su_dict.sort(key=lambda x: int(x.get("java")), reverse=asc_or_desc_bool)
    elif mode == 0:
        su_dict.sort(key=lambda x: int(x.get("english") + x.get("python") + x.get("java")), reverse=asc_or_desc_bool)
    else:
        print("Please enter right content, try again")
        sortStu()

    format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t"
    print(format_title.format("id", "name", "english", "python", "java", "total"))
    for stu in su_dict:
        total = int(stu["english"]) + int(stu["python"]) + int(stu["java"])
        print(format_title.format(stu["id"], stu["name"], stu["english"], stu["python"], stu["java"], total))


def countStu():
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as read:
            readStu = read.readlines()
            if readStu:
                print("There are {0} students in the school".format(len(readStu)))
            else:
                print("No student information available")
    else:
        print("No student information available")


def displayStu():
    if os.path.exists("students.txt"):
        res = []
        with open("students.txt", "r", encoding="utf-8") as read:
            readStu = read.readlines()
            if readStu:
                for item in readStu:
                    dit = dict(eval(item))
                    res.append(dit)
        if res:
            format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t"
            print(format_title.format("id", "name", "english", "python", "java", "total"))
            for stu in res:
                total = int(stu["english"]) + int(stu["python"]) + int(stu["java"])
                print(format_title.format(stu["id"], stu["name"], stu["english"], stu["python"], stu["java"], total))
        else:
            print("No student information available")
    else:
        print("No student information available")


if __name__ == '__main__':
    main()
