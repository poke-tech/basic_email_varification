import re
#email= input("Enter Your Email Here :")


# now lets make a function to make cheak the syntax of the email
def cheakONE(email):

    # this is the basic pattern of a email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    local_part, domain_part= email.split("@")
    if email.count("@")!=1:
        print("your email have a missing '@' ")

    local_pattern= r'^[a-zA-Z0-9._%+-]+$'

    if not re.match(local_pattern,local_part):
        print("the part befour the '@' is wrong cheak your email again")

    domain_pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(domain_pattern,domain_part):
        print("the part after '@ ' is wrong cheak your email again   ")

    if email.count(".")>1 :
        print("this gmail contain more that 1 '.' cheak the gmail again")
    else:
        if re.match(pattern,email):
            return True
email = input("Enter your email:")
if cheakONE(email):
    print("Email format is valid.")