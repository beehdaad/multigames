from .class_database import DataBase
from .custom_error import PasswordRange, AllowedWord


class register:
    """ 
    Creates an account using the username and password entered by the user
    which must follow some rules, otherwise it will raise an error
    """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if not isinstance(value, str):
            raise ValueError
        if not value[0].isalpha():
            raise AllowedWord
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        if not isinstance(value, str):
            raise ValueError
        if not 8 <= len(value) <= 12:
            raise PasswordRange
        self.__password = value

    def check_username(self, data: list[dict]):
        """
        It checks if the username already exists and returns false

        Parameters
        ----------
        data: list :
            User accounts data

        Returns
        -------
        User index in the database and a boolean

        """
        index: int = 0
        content: bool = False
        for account in data:
            if account["username"] == self.__username:
                content = True
                break
            index += 1
        return content, index

    def register(self, data: list[dict]):
        """
        If the username does not exist in the database, it will be written and the output will return True

        Parameters
        ----------
        data: list :
            User accounts data

        Returns
        -------
        boolean

        """
        content: bool = False
        if register.check_username(self, data)[0] is False:
            data.append(dict(username=self.__username, password=self.__password, wallet= 50)) # noqa E501
            DataBase.write_file(data)
            content = True
        return content


class login(DataBase):
    """ 
    If the username and password are in the database,
    it will allow login, otherwise it will return an error
    You can even log out of the account
    """
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self, data: list[dict]):
        """

        Parameters
        ----------
        data: list :
            User accounts list

        Returns
        -------
        Dictionary containing user information and boolean value

        """
        index: int = 0
        content: bool = False
        user: dict = dict()
        for account in data:
            if account["username"] == self.username:
                if account["password"] == self.password:
                    user = data.pop(index)
                    content = True
                    break
            index += 1
        return user, content

    def logout(self, data: list[dict], user_info: dict):
        """
        Added user information with the internal database and rewrote the database file
    
        Parameters
        ----------
        data: list :
            User accounts list
        user_info :
            Dictionary containing user information

        Returns
        -------

        """
        data.append(user_info)
        DataBase.write_file(data)


if __name__ == "__main__":
    ...
