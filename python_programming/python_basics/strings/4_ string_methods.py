name = "Bro Code"
print(name[1])
print(len(name))  # technically this is a function
print(type(len(name)))
print(name.find("o"))
print(name.find('n', 1, 10))  # (substring, start_index , end_index )
print(name.capitalize())
print(name.upper())
print(name.lower())
print( name.strip())  # like trim , returns a new string after removing any leading and trailing whitespaces including tabs (\t).
print(name.rstrip())  # line rtrim
print(name.ltrip())  # like l trim
print(name.isdigit())
print(name.isalpha())  # only alphabets without special char
print(name.count("o"))
print(name.replace("o", "a"))
print(name * 3)  # display name 3 times

name2 = "Nouman-27-python"
print(name2.split("-"))  # split items at given string and make list of them

full_name = "Syed.Nouman"
first_name, last_name = full_name.split(".")
print(first_name, last_name)

# ************************
# mobile = "0342-4556029"
# print(mobile.isdigit())
# print(mobile[:4].isdigit())
# print(mobile[5:].isdigit())

# print(mobile[4] != '-')
# print(len(mobile) != 12)
# print(mobile[:4].isdigit() is not True)
# print(mobile[5:].isdigit() is not True)
