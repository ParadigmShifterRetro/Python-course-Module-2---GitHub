#Test - modify this file in GitHub web interface before changing my local file

users = {"user1": "password1", "user2": "password2"}

# refactor: turn user name validation into a function since it will most likely be useful elsewhere
def validate_user(name):
    return name in users

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    #if username in users:
    if validate_user(username):
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Example usage
login()
