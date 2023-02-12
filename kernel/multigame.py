import logging
from os import system
import logging.config
from time import sleep

from tabulate import tabulate

from helper import (
    Table,
    LogMsg,
    command,
    OtherMsg,
    LoadingLogo,
    LoadingIcon,
    AllowedWord,
    PasswordRange,
)
from sqlalchemy.exc import IntegrityError
from .dungeon_and_dragon import dungeon_and_dragon
from database.models import User

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
                # -------------------------REGISTER PAGE-------------------------
                sleep(0.1)
                logger.info(LogMsg.register_main_section)
                loop_condition_register_page = True
                while loop_condition_register_page:
                    system("clear")
                    logger.info(LogMsg.register_section)
                    register_page = [[Table.description_return]]
                    print(tabulate(register_page, [Table.register_page.center(35)], tablefmt="heavy_grid"))
                    print(OtherMsg.username)
                    input_username = input(OtherMsg.icon_input).casefold()
                    if input_username.startswith("-"):
                        try:
                            user_command = command(input_username, ("-return",))
                        except ValueError:
                            logger.info(LogMsg.command_report_register.format(input_username))
                            print(OtherMsg.valid_command, "'-return'")
                            sleep(0.7)
                        else:
                            logger.info(LogMsg.return_register_section)
                            loop_condition_register_page = False
                    elif input_username[0].isalpha():
                        system("clear")
                        print(tabulate(register_page, [Table.register_page.center(35)], tablefmt="heavy_grid"))
                        print(f"Username: {input_username}")
                        input_password = input("Password: ")
                        try:
                            User.register(input_username, input_password)
                        except AllowedWord:
                            logger.info(LogMsg.warning_rules_user)
                            print(OtherMsg.warning_rules_user)
                            sleep(0.7)
                        except PasswordRange:
                            logger.info(LogMsg.warning_rules_pw)
                            print(OtherMsg.warning_rules_pw)
                            sleep(0.7)
                        except IntegrityError:
                            logger.info(LogMsg.duplicate_user.format(input_username))
                            print(OtherMsg.used_before_username)
                            sleep(0.7)
                        else:
                            logger.info(LogMsg.registered.format(input_username))
                            LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                            print(OtherMsg.successfully_registered)
                            sleep(0.7)
                            loop_condition_register_page = False
            elif input_command == "-login":
                # -------------------------LOGIN PAGE-------------------------
                sleep(0.1)
                logger.info(LogMsg.login_main_section)
                loop_condition_login_page = True
                while loop_condition_login_page:
                    system("clear")
                    logger.info(LogMsg.login_section)
                    login_page = [[Table.description_return]]
                    print(tabulate(login_page, [Table.login_page.center(35)], tablefmt="heavy_grid"))
                    print(OtherMsg.username)
                    input_username = input(OtherMsg.icon_input).casefold()
                    if input_username.startswith("-"):
                        try:
                            user_command = command(input_username, ("-return",))
                        except ValueError:
                            logger.info(LogMsg.command_report_login.format(input_username))
                            print(OtherMsg.valid_command, "'-return'")
                            sleep(0.7)
                        else:
                            logger.info(LogMsg.return_login_section)
                            loop_condition_login_page = False
                    elif input_username.isalpha():
                        system("clear")
                        print(tabulate(login_page, [Table.login_page.center(35)], tablefmt="heavy_grid"))
                        print(f"{OtherMsg.username} {input_username}")
                        input_password = input("Password: ")
                        acc = User.login(input_username, input_password)
                        if acc is not None:
                            wallet = acc[0].wallet
                            logger.info(LogMsg.login.format(input_username))
                            LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                            print(OtherMsg.username_login)
                            sleep(0.7)
                            # wallet = int(USER_INFORMATION["wallet"])
                            # -------------------------SELECT GAMES-------------------------
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
                                    user_command = command(input_command, ("-logout", "-dad", "-ttt", "-hm"))
                                except ValueError:
                                    logger.info(LogMsg.command_report_select_games.format(input_command))
                                    print(OtherMsg.valid_command, "'-logout' '-dad' '-ttt' '-hm'")
                                    sleep(0.7)
                                else:
                                    if input_command == "-logout":
                                        logger.info(LogMsg.logout_select_games_section.format(input_username, wallet))
                                        LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                                        loop_condition_select_games = False
                                        loop_condition_login_page = False
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
                                        User.update_wallet(input_username, wallet)
                        else:
                            logger.info(LogMsg.wrong_user_pw.format(input_username, input_password))
                            print(OtherMsg.wrong_user_pass)
                            sleep(0.7)
                    else:
                        logger.info(LogMsg.command_report_main.format(input_command))
                        print(OtherMsg.input_valid)
                        sleep(0.7)
    logger.info(LogMsg.end)
