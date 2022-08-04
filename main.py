import string
import random
import pyperclip

if __name__ == "__main__":
    lower_letters = list(string.ascii_lowercase)
    upper_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    while True:
        try:
            password_length = int(input("Enter the desired length of the password\n"))
            break;
        except ValueError:
            print("Please enter a valid password length in numbers")
    

    password_characters = []
    password_characters.extend(lower_letters)
    password_characters.extend(upper_letters)
    password_characters.extend(numbers)
    password_characters.extend(symbols)

    random.shuffle(password_characters)

    password = "".join(password_characters[0:password_length])

    pyperclip.copy(password)
    print("Your password has been copied to your clipboard")
    
