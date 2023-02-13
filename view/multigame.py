import logging
from os import system
import logging.config
from time import sleep

from tabulate import tabulate

from helper import (
    Table,
    LogMsg,
    OtherMsg,
    LoadingLogo,
)
from control.class_command import command
from .register import func_register
from .login import func_login
"""
The implementation of the program is from this part, which was written by nested loop
"""

logger = logging.getLogger(__name__)


def main():
    logger.info(LogMsg.start)
    LoadingLogo(OtherMsg.multi_games).show()
    loop_condition_main_page = True
    while loop_condition_main_page:
        # -------------------------MAIN PAGE-------------------------
        system("clear")
        logger.info(LogMsg.main_section)
        main_page = [
                    [Table.description_register],
                    [Table.description_login],
                    [Table.description_help],
                    ]
        print(tabulate(main_page, [Table.main_page.center(35)], tablefmt="heavy_grid"))
        input_command = input(OtherMsg.icon_input).casefold()
        try:
            user_command = command(input_command, ("-login", "-register", "-help", "-exit"))
        except ValueError:
            logger.info(LogMsg.command_report_main.format(input_command))
            print(OtherMsg.valid_command, "'-login' '-register' '-help' '-exit'")
            sleep(0.7)
        else:
            if input_command == "-help":
                logger.info(LogMsg.help_main_section)
                user_command.dash_help()
                input("Press 'enter' on the keyboard to exit -help ")
                system("clear")
            elif input_command == "-exit":
                logger.info(LogMsg.exit_main_section)
                user_command.dash_exit()
                loop_condition_main_page = False
            elif input_command == "-register":
                sleep(0.1)
                func_register(logger)
            elif input_command == "-login":
                sleep(0.1)
                func_login(logger)
            # else:
            #     logger.info(LogMsg.command_report_main.format(input_command))
            #     print(OtherMsg.input_valid)
            #     sleep(0.7)
    logger.info(LogMsg.end)
