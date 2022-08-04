import string, random, pyperclip, re
import sys

#function to generate a strong password
def generate_password(password_length : int) -> str :
    lower_letters = list(string.ascii_lowercase)
    upper_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    
    password_characters = []
    password_characters.extend(lower_letters)
    password_characters.extend(upper_letters)
    password_characters.extend(numbers)
    password_characters.extend(symbols)

    random.shuffle(password_characters)
    password = "".join(password_characters[0:password_length])

    return password

#function to get the strength of a password
def password_strength(password : str) -> str :
    password_length = len(password)
    uppercase_regex = re.compile(r"[A-Z]+")
    lowercase_regex = re.compile(r"[a-z]+")
    digits_regex = re.compile(r"\d+")
    special_regex = re.compile(r"\W+")

    upper_match = uppercase_regex.search(password)
    lower_match = lowercase_regex.search(password)
    digits_match = digits_regex.search(password)
    special_match = special_regex.search(password)

    if password_length > 8:
        if lower_match and digits_match and special_match :
            if upper_match :
                return "very-strong"
            else:
                return "strong"
        else:
            return "weak"
    else:
        if lower_match and digits_match and special_match and upper_match :
            return "medium"
        else:
            return "weak"


if __name__ == "__main__":
    print("Enter 1 to generate a new password")
    print("Enter 2 to check the strength of a password")
    print("Enter any other number to exit the program")

    choice = input("Enter your desired choice\n")
    password_length = 0
    password = ""

    if choice == "1":
        while True:
            try:
                password_length = int(input("Enter the desired length of the password\n"))
                break
            except ValueError:
                print("Please enter a valid choice")
        
        password = generate_password(password_length)
        pyperclip.copy(password)
        print("Your password has been copied to the clipboard")

    elif choice == "2":
        password = input("Enter the password whose strength is to be checked")
        print("your passowrd strength is ", password_strength(password))

    else:
        sys.exit()    