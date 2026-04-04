


valid_users = ['Hassan', 'Daniyal', 'Ibi','Ali']

print("LOGIN SYSTEM")

login_id = input("Login: ")


if login_id in valid_users:
    print("You are in!")
else:
    print("Access Denied! " + login_id + " is not a valid user.")


print("Done.")
