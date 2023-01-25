from .class_database import DataBase
from .custom_error import PasswordRange, AllowedWord


class register(DataBase):
    """ """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        """ """
        return self.__username

    @username.setter
    def username(self, value: str):
        """

        Parameters
        ----------
        value: str :
            

        Returns
        -------

        """
        if not isinstance(value, str):
            raise ValueError
        if not value[0].isalpha():
            raise AllowedWord
        self.__username = value

    @property
    def password(self):
        """ """
        return self.__password

    @password.setter
    def password(self, value: str):
        """

        Parameters
        ----------
        value: str :
            

        Returns
        -------

        """
        if not isinstance(value, str):
            raise ValueError
        if not 8 <= len(value) <= 12:
            raise PasswordRange
        self.__password = value

    def check_username(self, data: list):
        """

        Parameters
        ----------
        data: list :
            

        Returns
        -------

        """
        index: int = 0
        content: bool = False
        for account in data:
            if account["username"] == self.__username:
                content = True
                break
            index += 1
        return content, index

    def register(self, data: list):
        """

        Parameters
        ----------
        data: list :
            

        Returns
        -------

        """
        content: bool = False
        if register.check_username(self, data)[0] is False:
            data.append(dict(username=self.__username, password=self.__password, wallet= 50)) # noqa E501
            DataBase.write_file(data)
            content = True
        return content


class login(DataBase):
    """ """
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def login(self, data: list):
        """

        Parameters
        ----------
        data: list :
            

        Returns
        -------

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

    def logout(self, data: list, user_info):
        """

        Parameters
        ----------
        data: list :
            
        user_info :
            

        Returns
        -------

        """
        data.append(user_info)
        DataBase.write_file(data)


if __name__ == "__main__":
    ...
