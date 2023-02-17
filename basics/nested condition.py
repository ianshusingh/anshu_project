uname=input("Enter your name:")
email=input("Enter your email:")
pwd=input("enter password:")
pwd2=input("Confirm password:")
if len(uname)>=4 and len(uname)<16:
    if '@' in email and len(email)>6:
        if len(pwd)>=8 and len(pwd)<=20 and pwd != uname:
            if pwd==pwd2:
                print("uname Aceepted")
            else:
                print("password do not match")
        else:
            print("password invalid")
    else:
        print("Email invalid")
else:
    print("uname invalid")                            