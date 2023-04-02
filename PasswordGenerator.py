import random
import string

# Ask the user for the length of the password
length = int(input("Enter the desired length of the password (recommended minimum is 16): "))

# Define the characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the random password
password = ''.join(random.choice(characters) for i in range(length))

# Print the generated password
print("Generated password: ", password)
