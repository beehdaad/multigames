
from random import sample, choice
from os import system
from time import sleep
import math


class LevelEasy:
    def __init__(self) -> None:
        self.table_size = 5
        self.xy_list = [(x, y) for y in range(self.table_size) for x in range(self.table_size)]
        self.player, self.dragon, self.dungeon = sample(self.xy_list, k=3)
        self.wall = list()
        self.hint = tuple()


class LevelNormal:
    def __init__(self) -> None:
        self.table_size = 8
        self.xy_list = [(x, y) for y in range(self.table_size) for x in range(self.table_size)]
        self.player, self.dragon, self.dungeon, self.hint = sample(self.xy_list, k=4)
        self.wall = list()


class LevelHard:
    def __init__(self) -> None:
        self.table_size = 12
        self.xy_list = [(x, y) for y in range(self.table_size) for x in range(self.table_size)]
        self.player, self.dragon, self.dungeon, self.hint , *wall = sample(self.xy_list, k=25)
        self.wall = wall


class DrawMap:
    def __init__(self,table_size, xy_list, player,  wall, hint, dragon=None, dungeon=None, ) -> None:
        self.table_size = table_size
        self.xy_list = xy_list
        self.player = player
        self.dragon = dragon
        self.dungeon = dungeon
        self.wall = wall
        self.hint = hint
    def show(self):
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
    def check(table_size, character, wall) -> list[str]:
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
    def perform(self, check_distance) -> tuple[tuple[int, int], str]:
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
        output = "off"
        if math.dist(self.player, self.dragon) <= 2:
            output = 2
        elif math.dist(self.player, self.dragon) <= 4:
            output = 4
        return output


class HintDungeon:
    def play(dungeon):
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