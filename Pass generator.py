import random

# Step 1: Define all character types
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits    = "0123456789"
specials  = "!@#$%^&*"

# Step 2: Ask user for length
length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Length too short! Setting length to 8.")
    length = 8

# Step 3: Pick at least one from each type
char1 = random.choice(uppercase)
char2 = random.choice(lowercase)
char3 = random.choice(digits)
char4 = random.choice(specials)

# Step 4: Combine all characters
all_chars = uppercase + lowercase + digits + specials

# Step 5: Start password with the 4 guaranteed characters
password = [char1, char2, char3, char4]

# Step 6: Fill the rest randomly
for i in range(length - 4):
    password.append(random.choice(all_chars))

# Step 7: Shuffle so it doesn't look like a pattern
random.shuffle(password)

# Step 8: Convert list to string
final_password = ""
for char in password:
    final_password = final_password + char

# Step 9: Print the result
print("Your Password: " + final_password)