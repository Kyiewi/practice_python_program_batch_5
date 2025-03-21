# Ask user to input their full name in incorrect casing
user_name = input("Enter your full name in incorrect casing: ")

# Split user name
words = user_name.split()

# Convert name to snake_case
snake_name_case = '_'.join(word.lower() for word in words)

# Print output
print("Name:", snake_name_case)
