class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def crate_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def sum(x, y):
        return x + y


# c1 = Connection()
# # c1.set_user('Victor')
# print(c1.user)
# # c1.set_password('victor123')
# print(c1.password)


connection = Connection.crate_with_auth('victor', 'victor123')
print(connection.user)
print(connection.password)

print(Connection.sum(2, 3))