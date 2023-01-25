import csv
import os

from .settings import setting


class DataBase():
    """ """

    @staticmethod
    def read_file():
        """ """
        with open(setting._address.value, "r") as myfile:
            database = csv.DictReader(myfile)
            return [user for user in database]

    def write_file(INTERNAL_DATABASE: list):
        """

        Parameters
        ----------
        INTERNAL_DATABASE: list :
            

        Returns
        -------

        """
        with open(setting._address.value, "w") as myfile:
            database = csv.DictWriter(myfile, fieldnames=["username", "password", "wallet"]) # noqa E501
            database.writeheader()
            for line in INTERNAL_DATABASE:
                database.writerow(line)

    @staticmethod
    def check_existence_file():
        """ """
        list_dir = os.listdir("Accounts/")
        if setting._name.value not in list_dir:
            with open(setting._address.value, "w") as myfile:
                database = csv.DictWriter(myfile, fieldnames=["username", "password", "wallet"]) # noqa E501
                database.writeheader()


if __name__ == "__main__":
    ...
