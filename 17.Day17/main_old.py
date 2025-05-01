class User_test:
    
    def __init__(self):
        pass

user__ = User_test
user__.id = "001"
user__.name = "Srikrishna"

#print(user__.id)
#print(user__.name)

class User:  #Pascal case of naming
    
    def __init__(self, user_id, username):      # special function/method this is called a construct - initialise the attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user is being created...")
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "test")

user_1.follow(user_2)
print(user_1.followers) 
print(user_1.following)
print(user_2.followers)
print(user_2.following)


'''
#print(user_1.username)
#print(user_1.id)
#print(user_1.followers)

class Car:

    def __init__(self):
        self.seats = 4

    def enter_race_mode(self):
        self.seats = 5

my_car = Car()
print(my_car.seats)

my_car.enter_race_mode()
print(my_car.seats)

'''


