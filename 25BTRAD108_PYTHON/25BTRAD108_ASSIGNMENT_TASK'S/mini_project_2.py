import random

otp = random.randint(1000, 9999)

print("Generated OTP:", otp)

user_otp = int(input("Enter OTP: "))

if user_otp == otp:
    print("OTP Verified Successfully")
else:
    print("Invalid OTP”)
