import random
import string

url = input("Enter URL: ")

short = ''.join(random.choice(string.ascii_letters) for _ in range(6))

print("Short URL: short.ly/" + short)
