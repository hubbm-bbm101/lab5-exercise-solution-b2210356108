def email(text1):
    a=0
    b=0
    for i in text1:
        if i == "@":
            a+=1
        if i == ".":
            b+=1
    if a>0 and b>0:
        return True
    else:
        return False


text = str(input("write a string:"))
result = email(text)
if result == True:
    print("that is an email")
else:
    print("that is not an email")





