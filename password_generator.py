import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Characters to choose from
chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(chars) for i in range(length))

# Show it
print("Your password is:", password)
