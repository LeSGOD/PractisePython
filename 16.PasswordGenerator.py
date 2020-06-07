import random
import string


def password_generator(size):
    password = ''.join(random.choices(
        string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size))
    print(password)


password_generator(5)
