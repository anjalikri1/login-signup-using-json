import json 
import os
import re
print("Welcomr to my login/signup page :")
user=input("do you want (login/signup) :")
if user=="signup":
    name=input("enter your user name :")
    print("creat strong password :")
    pass1=input("create a password :")
    if re.search("[a-z A-Z]",pass1) and re.search("[@%$#!&*]",pass1) and re.search("[1-9]",pass1):
        pass2=input("re enter your password :")
        if pass1==pass2:
            print("password confirm")
            dob=input("enter your date of birth :")
            mob=int(input("enter your mobile number :"))
            email=input("enter your email address :")
            print("ypur account has been created successfully")
            print("procced to login by using your userid and password:")
            a={"userid":name,"password":pass1,"date of birth":dob,"mobile number":mob,"email address":email}
            f=open("signup.json","a")
            json.dump(a,f,indent=4)
        else:
            print("password not matched")
    else:
        print("Please create Strong password")
else:
    if user=="login":
        username=input("enter the user id :")
        password=input("enter the password :")
        if ["name"]==username and ["pass1"]==password:
            with open("signup.json","r") as file:
                json.load(file)
            print("login successfull")
        else:
            print("worng user name")
    else:
        print("worng user name")








    
