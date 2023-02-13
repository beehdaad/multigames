
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
from control.database import Query_DB
from .select_games import func_select_games

def func_login(logger):
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
                command(input_username, ("-return",))
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
            acc = Query_DB.login(input_username, input_password)
            if acc is not None:
                wallet = acc[0].wallet
                logger.info(LogMsg.login.format(input_username))
                LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                print(OtherMsg.username_login)
                sleep(0.7)
                func_select_games(logger, input_username, wallet)
                loop_condition_login_page = False
            else:
                logger.info(LogMsg.wrong_user_pw.format(input_username, input_password))
                print(OtherMsg.wrong_user_pass)
                sleep(0.7)