import random
import string

letters = [random.choice(string.ascii_uppercase) for _ in range(3)]

digits = [random.choice(string.digits) for _ in range(3)]

chars = "!@#$%^&*"
specials = [random.choice(chars) for _ in range(2)]

password_list = letters + digits + specials

random.shuffle(password_list)

password = "".join(password_list)

print("Ваш пароль:", password)
