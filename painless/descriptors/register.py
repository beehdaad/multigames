from helper import AllowedWord, PasswordRange

class UsernameDescriptor:
    def __init__(self, username) -> None:
        self.username = username

    def __get__(self, obj, owner):
        return obj.__dict__[self.username]

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError
        if not value[0].isalpha():
            raise AllowedWord
        obj.__dict__[self.username] = value


class PasswordDescriptor:
    def __init__(self, password) -> None:
        self.password = password
    def __get__(self, obj, owner):
        return obj.__dict__[self.password]
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError
        if not 8 <= len(value) <= 12:
            raise PasswordRange
        obj.__dict__[self.password] = value

if __name__ == "__main__":
    ...
