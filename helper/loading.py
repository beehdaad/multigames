from os import system
from time import sleep

import pyfiglet


class LoadingIcon:
    """
    Prints the desired text as a demonstration
    """
    def __init__(self, caption: str, time: float, count: int) -> None:
        self.caption = caption
        self.time = time
        self.count = count

    @property
    def caption(self):
        ...

    @caption.setter
    def caption(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__caption = value

    @property
    def time():
        ...

    @time.setter
    def time(self, value):
        if not isinstance(value, float):
            raise TypeError
        self.__time = value

    @property
    def count():
        ...

    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise TypeError
        self.__count = value

    def show(self):
        """
        By means of this function, the value of the object is taken and printed
        """
        num = 0
        while self.__count > num:
            system("clear")
            print(f"{self.__caption}.")
            sleep(self.__time)
            system("clear")
            print(f"{self.__caption}..")
            sleep(self.__time)
            system("clear")
            print(f"{self.__caption}...")
            sleep(self.__time)
            system("clear")
            num += 1


class LoadingLogo:
    """
    Prints a text as a logo and counting from 0 to 100
    """
    def __init__(self, caption) -> None:
        self.caption = caption

    @property
    def caption(self):
        return self.__caption

    @caption.setter
    def caption(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not len(value) < 20:
            raise ValueError
        self.__caption = value

    def show(self):
        """
        By means of this function, the value of the object is taken and printed
        """
        TXT_PYFIGLET = pyfiglet.Figlet(font='slant')
        count: int = 0
        while count < 30:
            system("clear")
            print(TXT_PYFIGLET.renderText(self.__caption))
            print(f"{'.'*(count)}{count}%{'.'*count}", end="")
            sleep(0.06)
            count += 1
        system("clear")
        print(TXT_PYFIGLET.renderText(self.__caption))
        print(f"{'.'*(30)}{100}%{'.'*(30)}", end="")
        sleep(0.2)
        system("clear")


class LoadingCountNum:
    """
    Counter 1 2 3 whose speed can be adjusted
    which is printed after calling
    """
    def __init__(self, time) -> None:
        self.time = time
        count = pyfiglet.Figlet(font='big')
        system("clear")
        print(count.renderText('1'))
        sleep(self.__time)
        system("clear")
        print(count.renderText('2'))
        sleep(self.__time)
        system("clear")
        print(count.renderText('3'))
        sleep(self.__time)
        system("clear")

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if not isinstance(value, float):
            raise TypeError
        self.__time = value


if __name__ == "__main__":
    LoadingLogo("Multi Games").show()
