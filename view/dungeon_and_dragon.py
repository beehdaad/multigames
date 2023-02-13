
from os import system
import logging
from time import sleep

import cowsay
from stringcolor import cs
from tabulate import tabulate

from helper import (
    Table,
    LogMsg,
    OtherMsg,
    LoadingCountNum,
)
from control.class_command import command
from control.dungeon_and_dragon import (
    DrawMap,
    LevelHard,
    LevelEasy,
    MoveDragon,
    HintDungeon,
    LevelNormal,
    MoveCharacter,
    AllowedDirection,
)
logger = logging.getLogger("dad")

def dungeon_and_dragon(username: str, wallet: int) -> int:
    loop_condition_dad_page = True
    while loop_condition_dad_page:
        system("clear")
        logger.info(LogMsg.dad_section.format(username, wallet))
        select_levels = [
                        [Table.description_easy],
                        [Table.description_normal],
                        [Table.description_hard]
                        ]
        print(f"{username}, you have {wallet}₵")
        print(tabulate(select_levels, [Table.dad_page.center(35)], tablefmt="heavy_grid"))
        input_command = input(OtherMsg.icon_input).casefold()
        try:
            user_command = command(input_command, ("-easy", "-normal", "-hard", "-adv", "-return"))
        except ValueError:
            logger.info(LogMsg.command_report_dad.format(username))
            print(OtherMsg.valid_command, "'-easy' '-normal' '-hard' '-adv' '-return'")
            sleep(0.7)
            system("clear")
        else:
            levels = {"-easy": (4, 7), "-normal": (10, 16), "-hard": (22, 40)}
            if input_command == "-adv":
                logger.info(LogMsg.adv_start_dad_section.format(username, wallet))
                coin = user_command.dash_adv(1.3)
                wallet += coin
                logger.info(LogMsg.adv_end_dad_section.format(username, wallet))
            elif input_command == "-return":
                loop_condition_dad_page = False
                logger.info(LogMsg.return_dad_section.format(username))
            elif input_command in levels:
                if input_command == "-easy" and wallet < 4:
                    print(OtherMsg.not_enough_coins, OtherMsg.suggest_adv)
                    sleep(1)
                elif input_command == "-normal" and wallet < 10:
                    print(OtherMsg.not_enough_coins, OtherMsg.suggest_adv)
                    sleep(1)
                elif input_command == "-hard" and wallet < 22:
                    print(OtherMsg.not_enough_coins, OtherMsg.suggest_adv)
                    sleep(1)
                else:
                    system("clear")
                    wallet -= levels[input_command][0]
                    logger.info(LogMsg.report_levels_1.format(username, input_command, levels[input_command][0], wallet))
                    print(OtherMsg.information_before_run_dad.format(username, levels[input_command][0], wallet))
                    input(OtherMsg.input_ready)
                    logger.info(LogMsg.report_levels_2.format(username, wallet))
                    LoadingCountNum(0.9)
                    # -------------------------PLAY GAME DUNGEON AND DRAGON-------------------------
                    if input_command == "-easy":
                        value = LevelEasy()
                    elif input_command == "-normal":
                        value = LevelNormal()
                    elif input_command == "-hard":
                        value = LevelHard()
                    logger.info(LogMsg.report_levels.format(username, input_command.lstrip("-"), wallet))
                    draw_map = DrawMap(value.table_size, value.xy_list, value.player, value.wall, value.hint)
                    loop_condition_dad_game = True
                    alarm = "off"
                    while loop_condition_dad_game:
                        system("clear")
                        if alarm == "hearing" and input_command != "-easy":
                            print(tabulate([[cs(Table.dragon_hearing, "red")]], tablefmt="grid"))
                        elif alarm == "smell" and input_command != "-easy":
                            print(tabulate([[cs(Table.dragon_smell, "yellow")]], tablefmt="grid"))
                        elif alarm == "off" and input_command != "-easy":
                            print(tabulate([[cs(Table.safe_place, "Green")]], tablefmt="grid"))
                        draw_map.show()
                        logger.info(LogMsg.report_map.format(value.player, value.dragon))
                        direction = AllowedDirection.check(value.table_size, value.player, value.wall)
                        move = input(f"{direction} : ").casefold()
                        if move in direction:
                            value.player = MoveCharacter(value.player, move).perform()
                            logger.info(LogMsg.report_player.format(draw_map.player, move, value.player))
                            draw_map.player = value.player
                            if not input_command == "-easy":
                                alarm = MoveDragon.distance(value)
                                if isinstance(alarm, int):
                                    value.dragon, alarm = MoveDragon.perform(value, alarm)
                                    logger.info(LogMsg.report_dragon.format(value.dragon))
                        if value.player == value.dragon:
                            system("clear")
                            cowsay.dragon("YOU LOSE!")
                            loop_condition_dad_game = False
                            logger.info(LogMsg.report_lose.format(username, wallet))
                            sleep(2)
                        elif value.player == value.dungeon:
                            system("clear")
                            cowsay.cow("YOU WON!")
                            print(cs(OtherMsg.congratulations.format(username, levels[input_command][1]), "green"))
                            loop_condition_dad_game = False
                            wallet += levels[input_command][1]
                            logger.info(LogMsg.report_won.format(username, levels[input_command][1], wallet))
                            sleep(2)
                        elif value.player == value.hint and input_command != "-easy":
                            draw_map.hint = None
                            value.hint = None
                            system("clear")
                            input("Please unmute your speaker\nPress 'enter' and listen carefully ")
                            # Tested with Mac OS
                            # If you get an error, comment the bottom line
                            HintDungeon.play(value.dungeon)
                            logger.info(LogMsg.report_hint.format(username))
    return wallet
