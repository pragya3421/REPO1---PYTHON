##Password Strength Checker

import re

##Password Strength Check Conditiond:
    #min 8 characters, digits, upper case, lower case, special character
    
def check_Password_strength(password):
    if len(password) < 8:       #length of password
        return "Weak Password-Password must be min 8 characters"

    if not any(char.isdigit() for char in password):
        return "Weak Password: Must contain a digit"

    if not any(char.isupper() for char in password):
        return "Weak Password: Must contain an upper character"
    
    if not any(char. islower() for char in password):
        return "Weak Password: Must contain a lower character"
    
    if not re.search(r"[^\w]", password):
        return "Medium Password: Password must contain at least one special character."
    
    return "Strong: Your Password is secured!"


##Now using it

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Thank You for using this tool")
            break

        result = check_Password_strength(password)
        print(result)

        
#Run the password checker tool

if __name__ == "__main__":
    password_checker()

