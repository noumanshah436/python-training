def input_phone_number(self):
    flag = True
    phone = None
    while flag:
        phone = input("Input Phone of  type Number of length = 10 i.e. XXXXXXXXXX :")
        # print(len(phone))
        if phone.isdigit():
            if len(phone) == 10:
                flag = False
    phone = int(phone)
    return phone


def input_mobile_number(self):
    flag = True
    while flag:
        mobile = input("Enter Mobile as XXXX-XXXXXXX:")
        if len(mobile) == 12:
            if mobile[4] == '-':
                if mobile[:4].isdigit():
                    if mobile[5:].isdigit():
                        flag = False
    return mobile



"""

mobile = input("enter Mobile as XXXX-XXXXXXX:")
while len(mobile) != 12:
    mobile = input("input Valid Mobile Number :")
print("valid length")
while mobile[4] != '-':
    mobile = input("input Valid Mobile Number :")
print("valid -")
while mobile[:4].isdigit() is not True:
    mobile = input("input Valid Mobile Number :")
print("valid 0-4")
while mobile[5:].isdigit() is not True:
    mobile = input("input Valid Mobile Number :")
print("valid 5:end")
print(mobile)

# ***********************
# while ((len(mobile) != 12) and (mobile[4] != '-') and (mobile[:4].isdigit() is not True)
#        and (mobile[5:].isdigit() is not True)):
#     mobile = input("input Valid Mobile Number :")

# ***********************



# *******************************

#  input valid phone 042XXXXXXX  length =10 and store in number

flag = True
phone=None
while flag:
    try:
        phone = input("Input Phone of  type Number of length = 10 i.e. XXXXXXXXXX :")
        print(len(phone))
        while len(phone) != 10:
            print("Invalid Length:")
            phone = input("Input Phone of  type Number of length = 10 i.e. XXXXXXXXXX :")
        phone = int(phone)
        flag = False
    except ValueError:
        print("Invalid Number")
        pass


print(phone)

"""