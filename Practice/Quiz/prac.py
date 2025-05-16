class User:   # note every first letter of the class is capitalised
    #pass    #if we do not want any code here 
    def __init__(self, user_id, username):   # not called a functrion but a method, as it is defined inside a class
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.gender = "male"
    
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Krish")     # creating an object from the class
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# user_2.id = "002"
# user_2.username = "krish2.0"


# other way is to use constructor



