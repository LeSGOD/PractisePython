"""
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

"""

import string


def get_validity_password(passwords):
    passwords = passwords.split(",")
    lower = ",".join(string.ascii_lowercase).split(",")
    upper = ",".join(string.ascii_uppercase).split(",")
    superChar = ["$", "#", "@"]
    numbers = [str(i) for i in range(10)]

    password_list = []
    for password in passwords:

        result = password
        password = [str(i) for i in set(map(str, password))]
        if 6 <= len(password) <= 12:
            if any(elem in password for elem in lower) and any(elem in password for elem in upper) and any(elem in password for elem in superChar) and any(elem in password for elem in numbers):
                password_list.append(result)

    return ",".join(password_list)


print(get_validity_password("ABd1234@1,a F1#,2w3E*,2We3345"))



