
from os import system

from time import sleep

from tabulate import tabulate

from helper import (
    Table,
    LogMsg,
    OtherMsg,
    LoadingIcon,
)
from control.class_command import command
from .dungeon_and_dragon import dungeon_and_dragon
from control.database import Query_DB


def func_select_games(logger, input_username, wallet):
    loop_condition_select_games = True
    while loop_condition_select_games:
        logger.info(LogMsg.select_games_section)
        system("clear")
        print()
        select_games = [
                        [Table.description_hm],
                        [Table.description_ttt],
                        [Table.description_dad]
                        ]
        print(f"Hi, {input_username}")
        print(tabulate(select_games, [Table.select_games.center(25)], tablefmt="heavy_grid"))
        input_command = input(OtherMsg.icon_input)
        try:
            command(input_command, ("-logout", "-dad", "-ttt", "-hm"))
        except ValueError:
            logger.info(LogMsg.command_report_select_games.format(input_command))
            print(OtherMsg.valid_command, "'-logout' '-dad' '-ttt' '-hm'")
            sleep(0.7)
        else:
            if input_command == "-logout":
                logger.info(LogMsg.logout_select_games_section.format(input_username, wallet))
                LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                loop_condition_select_games = False
            elif input_command == "-hm":
                logger.info(LogMsg.hm_select_games_section)
                print("page not found")
                sleep(1)
            elif input_command == "-ttt":
                logger.info(LogMsg.ttt_select_games_section)
                print("page not found")
                sleep(1)
            elif input_command == "-dad":
                sleep(0.1)
                logger.info(LogMsg.dad_select_games_section)
                wallet = dungeon_and_dragon(input_username, wallet)
                Query_DB.update_wallet(input_username, wallet)
