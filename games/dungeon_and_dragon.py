
from random import sample, choice
from os import system
from time import sleep
import math


class LevelEasy:
    """
    Easy to make appropriate level values    
    """
    def __init__(self) -> None:
        self.table_size = 5
        self.xy_list = [(x, y) for y in range(self.table_size) for x in range(self.table_size)]
        self.player, self.dragon, self.dungeon = sample(self.xy_list, k=3)
        self.wall = list()
        self.hint = tuple()


class LevelNormal:
    """
    Normal to make appropriate level values    
    """
    def __init__(self) -> None:
        self.table_size = 8
        self.xy_list = [(x, y) for y in range(self.table_size) for x in range(self.table_size)]
        self.player, self.dragon, self.dungeon, self.hint = sample(self.xy_list, k=4)
        self.wall = list()


class LevelHard:
    """
    Hard to make appropriate level values    
    """
    def __init__(self) -> None:
        self.table_size = 12
        self.xy_list = [(x, y) for y in range(self.table_size) for x in range(self.table_size)]
        self.player, self.dragon, self.dungeon, self.hint , *wall = sample(self.xy_list, k=25)
        self.wall = wall


class DrawMap:
    """ 
    Create an initializer with an object from the leveling class
    
    For example:    
    >>> a = LevelsEasy()
    >>> b = DrawMap(a.table_size, a.xy_list, ...)
    And then we can use the show function and print its values with 
    
    >>> b.show()
    >>> show place game
    """
    def __init__(
                self,
                table_size: int,
                xy_list: list[tuple[int, int]],
                player: tuple[int, int],
                wall: list[tuple[int, int]],
                hint: tuple[int, int],
                dragon: tuple[int, int]=None,
                dungeon: tuple[int, int]=None
                ) -> None:
        self.table_size = table_size
        self.xy_list = xy_list
        self.player = player
        self.dragon = dragon
        self.dungeon = dungeon
        self.wall = wall
        self.hint = hint
    def show(self):
        """ 
        The output uses the print() function
        """
        print("-"*((self.table_size*3) + 2))
        for item in self.xy_list:
            x, y = item
            if x == 0:
                print("|", end="")
            if item == self.player:
                print(" 유", end="")
            elif item == self.dragon:
                print(" D ", end="")
            elif item == self.hint:
                print(" ? ", end="")
            elif item == self.dungeon:
                print(" O ", end="")
            elif item in self.wall:
                print(" ▒ ", end="")
            else:
                print("   ", end="")
            if x == (self.table_size-1):
                print("|")
                if y != (self.table_size-1):
                    print("-"+" "*(self.table_size*3)+"-")
        print("-"*((self.table_size*3) + 2))


class AllowedDirection:
    """ 
    Using the object you made from the game level,
    give the size of the table, character and walls to the function,
    Here you don't need to create object class Just call and pass the values into the function
    For Example:

    >>> list = AllowedDirection.check(values...)

    The output is the allowed value of the directions in a list

    >>> ["up", "down", "left", "right"]
    """
    def check(
            table_size: int,
            character: tuple,
            wall: list[tuple[int, int]]
            ) -> list[str]:
        """

        Parameters
        ----------
        table_size :
            The size of the game table to determine the character's range of motion
        character :
            The position of the game character, whether it is a player or a Dargon
        wall :
            It may not be a wall in the game, but if it is, it determines the range of the character's movement

        Returns
        -------
        list of directions

        """
        NAVIGATION = ["up", "down", "left", "right"]
        x_line, y_column = character
        if x_line == table_size-1:
            NAVIGATION.remove("right")
        if y_column == table_size-1:
            NAVIGATION.remove("down")
        if y_column == 0:
            NAVIGATION.remove("up")
        if x_line == 0:
            NAVIGATION.remove("left")
        if (x_line+1, y_column) in wall:
            NAVIGATION.remove("right")
        if (x_line-1, y_column) in wall:
            NAVIGATION.remove("left")
        if (x_line, y_column-1) in wall:
            NAVIGATION.remove("up")
        if (x_line, y_column+1) in wall:
            NAVIGATION.remove("down")
        return NAVIGATION


class MoveCharacter:
    """ 
    You have to give it the position of the character and the direction of movement,
    and its output will be a tuple by the perform function
    In fact, it changes the position of the character
    """
    def __init__(self, character: tuple[int, int], move: str) -> None:
        self.character = character
        self.move = move
    @property
    def character(self):
        return self.__character
    @character.setter
    def character(self, value):
        if not isinstance(value, tuple):
            raise TypeError
        self.__character = value
    
    @property
    def move(self):
        return self.__move
    @move.setter
    def move(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__move = value

    def perform(self) -> tuple[int, int]:
        """
        The output of this function after calling is the changed position of the character
        
        For example:

        >>> MoveCharacter((2, 5), "up").perform()
        >>> return -> (1, 5)
        """
        x_line, y_column = self.character
        if self.move == "up":
            y_column -= 1
        elif self.move == "down":
            y_column += 1
        elif self.move == "left":
            x_line -= 1
        elif self.move == "right":
            x_line += 1
        return (x_line, y_column)


class MoveDragon:
    """ 
    Dragon decides according to its current position, 
    you just need to use the perfom function and provide the required values to it.
    """
    def perform(self, check_distance: int | str) -> tuple[tuple[int, int], str]:
        """

        Parameters
        ----------
        check_distance :
            It is responsible for detecting the movement of the dragon

        Returns
        -------
            a tuple and a message from Dragon
            The message is None if the dragon has not moved
        """
        dragon_position = self.dragon, None
        NAVIGATION = AllowedDirection.check(self.table_size, self.dragon, self.wall)
        x_player, y_player = self.player
        x_dragon, y_dragon = self.dragon
        if check_distance == 2:
            if y_player == y_dragon and "left" in NAVIGATION and x_player < x_dragon: # noqa E501
                dragon_position = MoveCharacter(self.dragon, "left").perform(), "hearing"
            elif y_player == y_dragon and "right" in NAVIGATION and x_player > x_dragon: # noqa E501
                dragon_position = MoveCharacter(self.dragon, "right").perform(), "hearing"
            elif x_player == x_dragon and "up" in NAVIGATION and y_player < y_dragon: # noqa E501
                dragon_position = MoveCharacter(self.dragon, "up").perform(), "hearing"
            elif x_player == x_dragon and "down" in NAVIGATION and y_player > y_dragon: # noqa E501
                dragon_position = MoveCharacter(self.dragon, "down").perform(), "hearing"
            else:
                move = choice(NAVIGATION)
                dragon_position =  MoveCharacter(self.dragon, move).perform(), "hearing"
        elif check_distance == 4:
            move = choice(NAVIGATION)
            dragon_position =  MoveCharacter(self.dragon, move).perform(), "smell"
        return dragon_position

    def distance(self):
        """ 
        Calculate the distance between the player and
        the dragon using the Euclidean triangle method

        The object of the game is given to this function and
        it returns the distance of 2 or 4 or 'off' at the exit
        """
        output = "off"
        if math.dist(self.player, self.dragon) <= 2:
            output = 2
        elif math.dist(self.player, self.dragon) <= 4:
            output = 4
        return output


class HintDungeon:
    """
    Returns the position of the dungeon as a sound

    Tested on Mac OS
    """
    def play(dungeon: tuple[int, int]):
        """

        Parameters
        ----------
        dungeon :
            Dungeon location

        Returns
        -------
        Output only beep beep
        """
        x, y = dungeon
        file = "helper/Beep.mp3"
        for i in range(x):
            system("afplay " + file)
        sleep(1)
        for i in range(y):
            system("afplay " + file)
        sleep(1)
        system("clear")


if __name__ == "__main__":
    ...