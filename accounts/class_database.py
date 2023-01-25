import os
import csv

from .settings import setting


class DataBase():
    """ 
    This class consists of three methods that are responsible for the database
    """

    @staticmethod
    def read_file() -> list[dict]:
        """
        It reads the csv file line by line and returns it in a list in the output
        which is the output of user accounts in the form of a dictionary
        """
        with open(setting._address.value, "r") as myfile:
            database = csv.DictReader(myfile)
            return [user for user in database]

    def write_file(INTERNAL_DATABASE: list[dict]):
        """
        It takes a list containing user information in the form of a dictionary and rewrites an old csv file

        Parameters
        ----------
        INTERNAL_DATABASE:
            A list containing accounts that are in the dictionary

        """
        with open(setting._address.value, "w") as myfile:
            database = csv.DictWriter(myfile, fieldnames=["username", "password", "wallet"]) # noqa E501
            database.writeheader()
            for line in INTERNAL_DATABASE:
                database.writerow(line)

    @staticmethod
    def check_existence_file():
        """ 
        Checks that the csv file is created if it does not exist in the directory
        """
        list_dir = os.listdir("Accounts/")
        if setting._name.value not in list_dir:
            with open(setting._address.value, "w") as myfile:
                database = csv.DictWriter(myfile, fieldnames=["username", "password", "wallet"]) # noqa E501
                database.writeheader()


if __name__ == "__main__":
    ...
