import random
#for loop


from turtledemo.penrose import start

obj = [2, 3, 5, 7, 9]
for iterable in obj:
    print(iterable * 2)


# sum of First natural numbers
for i in range (0, 21, 2):
    print(i)


#Fizz Buzz
for iterable in range (1, 31):
    fizz = "Fizz"
    buzz = "Buzz"
    if iterable % 3 == 0 and iterable % 5 != 0:
        print(fizz)
    elif iterable % 5 == 0 and iterable % 3 != 0:
        print(buzz)
    elif iterable % 3 == 0 and iterable % 5 == 0:
        print(fizz + buzz)
    else:
        print(iterable)

#Response
    response = 500
    if response == 200:
        print("✅ OK")
    elif response == 401:
        print("🔒 Unauthorized")
    elif response == 500:
        print("💥 Server Error")
    else:
        print("❓ Unknown status")

    #Mission #2: Double-layered access check
    is_logged_in = False
    is_admin = False
    if is_logged_in and is_admin:
        print("Access granted")
    elif is_logged_in and not is_admin:
        print("Access limited")
    else:
        print("Access denied")

test_cases = [
        "Login with valid credentials",
        "Login with invalid password",
        "Password reset with email",
        "Password reset with invalid email",
        "Logout after session"
]
for index, case in enumerate(test_cases, start = 1):
    print(f"Running Test Case {index}: {case}")

#dicts

dictionary = {
    "name": "Victor",
    "email": "carl4welps@gmail.com",
    "role": "Admin",
    "is_active": True

}
for key, value in dictionary.items():

    print(f"Key: {key}", "—", f"Value: {value}")
print(f"Total fields: {len(dictionary)}")

