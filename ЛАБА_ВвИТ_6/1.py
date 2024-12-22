class UserAccount():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        print(password == self.__password)

user = UserAccount('Vladimir', 'emailemail@email', '12345678')
user.set_password('qwerty')
user.check_password('12345678')