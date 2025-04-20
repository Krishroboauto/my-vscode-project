class User:  #Pascal case of naming
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print("new user is being created...")

user_1 = User("001", "Angela")



print(user_1.username)
print(user_1.id)


