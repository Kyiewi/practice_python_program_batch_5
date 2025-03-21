#Ask User to input their full name
user_name = input("Enter your full name in incorrect casing: ")

#Split user name
words = user_name.split()

#Convert to name to pascal case
pascal_name_case = ""
for word in words:
    pascal_name_case += word.capitalize()

#Print Output
print("Name:", pascal_name_case)
