import random

def captchagenerator(n):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    captcha = ""  # Initialize an empty string to store the captcha
    while n:
        captcha += chrs[random.randint(0,61)]  # Use 0 as the start index, not 1
        n -= 1
    return captcha

def captchacheck(captcha, user_captcha):
    if captcha == user_captcha:
        return True
    return False

captcha = captchagenerator(5)
print("captcha is:", captcha)
print("Enter above captcha:")
usr_captcha = input()
if captchacheck(captcha, usr_captcha):
    print("CAPTCHA matched")
else:
    print("CAPTCHA is not matched")