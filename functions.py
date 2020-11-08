import re
import json
from datetime import datetime



class User:
    def __init__(self,f_name,l_name,email,password,mobile):
        self.f_name=f_name
        self.l_name=l_name
        self.email=email
        self.password=password
        self.mobile=mobile


    def convert_to_dict(self):
        return {f"{self.f_name}":{"f_name":self.f_name,"l_name":self.l_name,"email":self.email,"password":self.password,"mobile":self.mobile}}

    def save_user(self,data):
        f=open("users.txt","r")
        data_from_file=f.read()
        if data_from_file == "":
            f=open("users.txt","w")
            data_to_file=json.dumps(data)
            f.write(data_to_file)
            f.close()
        else:
            data_from_file=json.loads(data_from_file)
            data_from_file[f"{self.f_name}"]={"f_name":self.f_name,"l_name":self.l_name,"email":self.email,"password":self.password,"mobile":self.mobile}
            f=open("users.txt","w")
            data_to_file=json.dumps(data_from_file)
            f.write(data_to_file)
            f.close()

    def user_is_exists(self):
        f=open("users.txt","r")
        data_from_file=f.read()
        if data_from_file == "":
            return False
        else:
            data_from_file=json.loads(data_from_file)
            if self.f_name in data_from_file:
                return True
            else:
                return False



class Project:
    def __init__(self,title,details,total_target,start_date,end_date,owner):
        self.title=title
        self.details=details
        self.total_target=total_target
        self.start_date=start_date
        self.end_date=end_date
        self.owner=owner

    def convert_to_dict(self):
        return {f"{self.title}":{"details":self.details,"total_target":self.total_target,"start_date":self.start_date,"end_date":self.end_date,"owner":self.owner}}

    def save_pro(self,data):
        f=open("projects.txt","r")
        data_from_file=f.read()
        if data_from_file == "":
            f=open("projects.txt","w")
            data_to_file=json.dumps(data)
            f.write(data_to_file)
            f.close()
        else:
            data_from_file=json.loads(data_from_file)
            data_from_file[f"{self.title}"]={"details":self.details,"total_target":self.total_target,"start_date":self.start_date,"end_date":self.end_date,"owner":self.owner}
            f=open("projects.txt","w")
            data_to_file=json.dumps(data_from_file)
            f.write(data_to_file)
            f.close()


def pro_is_exists(pro):
        f=open("projects.txt","r")
        data_from_file=f.read()
        if data_from_file == "":
            return False
        else:
            data_from_file=json.loads(data_from_file)
            if pro in data_from_file:
                return True
            else:
                return False


def is_alpha(text):
    return text.isalpha()

def is_digit(text):
    return text.isdigit()

def have_value(text):
    if len(text) != 0:
        return True

def convert_to_date(string):
    date=datetime.strptime(string,"%d-%m-%Y").date()
    return date

def is_valid_mail(text):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", text) == None:
        return True

def is_valid_date(text):
    if not re.search("^(0[1-9]|1[0-9]|2[0-9]|3[0-9])(/|-)(0[1-9]|1[0-2])(/|-)20[0-9][0-9]$", text) == None:
        return True

def is_valid_mobile(text):
    if not re.match(r"(^011|012|015|010)+\d{8}", text) == None:
        return True

def is_passwords_match(password,c_password):
    if password==c_password:
        return True

def Form_User():
    print("…………………………………………………………………………|")
    print("**** Regstriation Form **** |")
    print("…………………………………………………………………………|")
    f_name=input("First Name : ")
    while not is_alpha(f_name) or not have_value(f_name):
        print("Name not valid")
        f_name=input("First Name : ")

    l_name=input("Last Name : ")
    while not is_alpha(l_name) or not have_value(l_name):
        print("Name not valid")
        l_name=input("Last Name : ")

    email=input("Email : ")
    while not have_value(email) or not is_valid_mail(email):
        print("email not valid")
        email=input("Email : ")

    password=input("Password : ")
    while not have_value(password):
        print("Valid Password , Try Again")
        password=input("Password : ")

    confirm_password=input("Confirm Password : ")
    while not is_passwords_match(password,confirm_password):
        print("Password Not match")
        confirm_password=input("Confirm Password : ")

    mobile=input("Mobile : ")
    while not is_digit(mobile) or not have_value(mobile) or not is_valid_mobile(mobile):
        print("mobile not valid")
        mobile=input("Mobile : ")

    user1 = User(f_name=f_name,l_name=l_name,email=email,password=password,mobile=mobile)
    if not user1.user_is_exists():
        user1.save_user(user1.convert_to_dict())
        print("…………………………………………………………………………………………|")
        print("**** Data Saved Successfully **** |")
        print("…………………………………………………………………………………………|")
        import Start
    else:
        print("😎😎😎😎 User is exists 😎😎😎😎")
        import Start

def login():
    global name
    print("……………………………………………|")
    print("**** Login  **** |")
    print("……………………………………………|")
    name=input("Enter User Name : ")
    password=input("Enter Password : ")
    f=open("users.txt","r")
    data_from_file=f.read()
    data_from_file=json.loads(data_from_file)
    if name in data_from_file :
        if password == data_from_file[f"{name}"]["password"]:
           #print("you logged in")
           import projects
           projects.pro_page()
        else:
            print("password incorrect")
            login()
    else:
        print("user name not found")
        import Start


def Create_Pro():
    print("…………………………………………………………………………|")
    print("**** Create project **** |")
    print("…………………………………………………………………………|")

    title=input("Enter title of project : ")
    while not is_alpha(title) or not have_value(title):
        print("title not valid")
        title=input("Enter title of project : ")

    details=input("Enter deatils about project : ")
    while not have_value(details):
        print("details not valid")
        details=input("Enter deatils about project : ")

    total_target=input("Enter total target of project : ")
    while not is_digit(total_target) or not have_value(total_target) :
        print("total not valid")
        total_target=input("Enter total target of project : ")

    start_date=input("Enter start date for project (dd-mm-yyyy) : ")
    while  not have_value(start_date) or not is_valid_date(start_date):
        print("Enter Date With Correct format")
        start_date=input("Enter start date for project (dd-mm-yyyy) : ")

    end_date=input("Enter end date for project (dd-mm-yyyy) : ")
    while  not have_value(end_date) or not is_valid_date(end_date):
        print("Enter Date With Correct format")
        end_date=input("Enter end date for project (dd-mm-yyyy) : ")


    pro1 = Project(title=title,details=details,total_target=total_target,start_date=start_date,end_date=end_date,owner=name)
    # print(pro1.convert_to_dict())
    if not pro_is_exists(title):
        pro1.save_pro(pro1.convert_to_dict())
        print("…………………………………………………………………………………………|")
        print("**** Data Saved Successfully **** |")
        print("…………………………………………………………………………………………|")
        import projects
        projects.pro_page()
    else:
        print("project is exists")
        import projects
        projects.pro_page()

def View_Pro():
    print("……………………………………………………………………………|")
    print("**** View all projects  **** |")
    print("……………………………………………………………………………|")
    f=open("projects.txt","r")
    data_from_file=f.read()
    if not data_from_file =="":
        data_from_file=json.loads(data_from_file)
        for key in data_from_file :
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|title        |{key}                                       ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|Owner        |{data_from_file[key]['owner']}              ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|details      |{data_from_file[key]['details']}            ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|total target |{data_from_file[key]['total_target']}       ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|start date   |{data_from_file[key]['start_date']}         ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|end date     |{data_from_file[key]['end_date']}           ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
        import projects
        projects.pro_page()
    else:
        print("no Projects found")
        import projects
        projects.pro_page()
       
    
def delete_Pro():
    print("……………………………………………………………………………|")
    print("**** Delete projects  **** |")
    print("……………………………………………………………………………|")
    del_pro=input("Enter title of project for Delete it :")
    if pro_is_exists(del_pro):
        f=open("projects.txt","r")
        data_from_file=f.read()
        data_from_file=json.loads(data_from_file)
        if data_from_file[f"{del_pro}"]["owner"] == name:
            data_from_file.pop(f"{del_pro}")

            f=open("projects.txt","w")
            data_to_file=json.dumps(data_from_file)
            f.write(data_to_file)
            f.close()

            print("Project deleted Successfully")
            import projects
            projects.pro_page()
        else:
            print("you can delete your projects only")
            import projects
            projects.pro_page()
    else:
        print("project not exists")
        import projects
        projects.pro_page()

def edit_Pro():
    print("……………………………………………………………………………|")
    print("**** Edit projects  **** |")
    print("……………………………………………………………………………|")
    edit_pro=input("Enter title of project for edit it :")
    if pro_is_exists(edit_pro):
        f=open("projects.txt","r")
        data_from_file=f.read()
        data_from_file=json.loads(data_from_file)
        if data_from_file[f"{edit_pro}"]["owner"] == name:
            data_from_file.pop(f"{edit_pro}")

            f=open("projects.txt","w")
            data_to_file=json.dumps(data_from_file)
            f.write(data_to_file)
            f.close()

            title=input("Enter title of project : ")
            while not is_alpha(title) or not have_value(title):
                print("title not valid")
                title=input("Enter title of project : ")

            details=input("Enter deatils about project : ")
            while not have_value(details):
                print("details not valid")
                details=input("Enter deatils about project : ")

            total_target=input("Enter total target of project : ")
            while not is_digit(total_target) or not have_value(total_target) :
                print("total not valid")
                total_target=input("Enter total target of project : ")

            start_date=input("Enter start date for project (dd-mm-yyyy) : ")
            while  not have_value(start_date) or not is_valid_date(start_date):
                print("Enter Date With Correct format")
                start_date=input("Enter start date for project (dd-mm-yyyy) : ")

            end_date=input("Enter end date for project (dd-mm-yyyy) : ")
            while  not have_value(end_date) or not is_valid_date(end_date):
                print("Enter Date With Correct format")
                end_date=input("Enter end date for project (dd-mm-yyyy) : ")


            pro1 = Project(title=title,details=details,total_target=total_target,start_date=start_date,end_date=end_date,owner=name)
            # print(pro1.convert_to_dict())

            pro1.save_pro(pro1.convert_to_dict())
            print("…………………………………………………………………………………………|")
            print("**** Data Edited Successfully **** |")
            print("…………………………………………………………………………………………|")
            import projects
            projects.pro_page()
        else:
            print("you can edit your projects only")
            import projects
            projects.pro_page()
    else:
        print("project not exists")
        import projects
        projects.pro_page()

def search_date():
    print("……………………………………………………………………………|")
    print("**** Search projects  **** |")
    print("……………………………………………………………………………|")
    date=input("Enter date for project (dd-mm-yyyy) : ")
    while  not have_value(date) or not is_valid_date(date):
        print("Enter Date With Correct format")
        date=input("Enter start date for project (dd-mm-yyyy) : ")
    search={}   
    f=open("projects.txt","r")
    data_from_file=f.read()
    data_from_file=json.loads(data_from_file)
    for key in data_from_file.keys():
        if convert_to_date(data_from_file[key]["start_date"]) <= convert_to_date(date) and convert_to_date(data_from_file[key]["end_date"]) >= convert_to_date(date):
            search[f"{key}"]=data_from_file[key]
            
    if len(search) > 0:
        for key in search :
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|title        |{key}                                       ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|Owner        |{data_from_file[key]['owner']}              ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|details      |{data_from_file[key]['details']}            ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|total target |{data_from_file[key]['total_target']}       ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|start date   |{data_from_file[key]['start_date']}         ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
            print(f"|end date     |{data_from_file[key]['end_date']}           ")
            print("|…………………………………|……………………………………………………………………………………………………………………")
        import projects
        projects.pro_page()
    else:
        print("not found any projects")
        import projects
        projects.pro_page()

