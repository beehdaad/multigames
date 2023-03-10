from os import system
from time import sleep

from cowsay import cow, fox

from helper.captions import DashMsg


class command:
    """
    It takes a list of comments and puts it as its key, and if it recognizes it, it creates an intense
    """

    def __init__(self, command: str, valid_command: list[str]) -> None:
        self.command = command
        self.valid_command = valid_command

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.startswith("-"):
            raise ValueError
        self.__command = value

    @property
    def valid_command(self):
        return self.__valid_command

    @valid_command.setter
    def valid_command(self, value):
        if not isinstance(value, tuple):
            raise TypeError
        if self.__command not in value:
            raise ValueError
        self.__valid_command = value

    def dash_exit(self):
        """
        The program end message is printed
        """
        if not self.__command == "-exit":
            raise ValueError
        system("clear")
        print(DashMsg.exit)
        sleep(2)
        system("clear")

    def dash_adv(self, speed: float):
        """
        A series of images are printed at a set speed for advertising purposes

        Parameters
        ----------
        speed: float :
            Print speed

        Returns
        -------
        The output returns 5 as the reward

        """
        if not self.__command == "-adv":
            raise ValueError
        system("clear")
        fox(DashMsg.adv_0.value)
        sleep(speed)
        system("clear")
        cow(DashMsg.adv_1.value)
        sleep(speed)
        system("clear")
        fox(DashMsg.adv_2.value)
        sleep(speed)
        system("clear")
        cow(DashMsg.adv_3.value)
        sleep(speed)
        system("clear")
        fox(DashMsg.adv_4.value)
        sleep(speed)
        system("clear")
        cow(DashMsg.adv_5.value)
        sleep(speed)
        system("clear")
        fox(DashMsg.adv_6.value)
        sleep(speed)
        system("clear")
        cow(DashMsg.adv_7.value)
        sleep(speed)
        system("clear")
        fox(DashMsg.adv_8.value)
        sleep(speed)
        system("clear")
        cow(DashMsg.adv_9.value)
        sleep(speed)
        system("clear")
        return 5

    def dash_help(self):
        """
        Prints a message about the program
        """
        if not self.__command == "-help":
            raise ValueError
        system("clear")
        print("-"*79)
        print(DashMsg.help.value)
        print("-"*79)


if __name__ == "__main__":
    ...
