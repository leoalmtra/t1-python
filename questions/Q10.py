import utils

while True:

    password = input("Type the password: ")

    pass_rules = [(lambda password: len(password) >= 8, "The password must have at least 8 characters."),
                (lambda c: any(c.isupper() for c in password),"The password must contain a uppercase character"),
                (lambda c: any(c.islower() for c in password),"The password must contain a lowercase character"),
                (lambda c: any(c.isdigit() for c in password),"The password must contain a number"),
                (lambda c: any(c in "!@#$%" for c in password),"The password must contain one of the listed: '!@#$%'")
                ]

    if not utils.validation(password,pass_rules):
        print("Invalid password.")
        continue
    else:
        break

print("Password created successfully.")