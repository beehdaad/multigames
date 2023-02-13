
from os import system

from time import sleep

from tabulate import tabulate

from helper import (
    Table,
    LogMsg,
    OtherMsg,
    LoadingIcon,
    AllowedWord,
    PasswordRange,
)
from control.class_command import command
from sqlalchemy.exc import IntegrityError
from control.database import Query_DB


def func_register(logger):
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
                command(input_username, ("-return",))
            except ValueError:
                logger.info(LogMsg.command_report_register.format(input_username))
                print(OtherMsg.valid_command, "'-return'")
                sleep(0.7)
            else:
                logger.info(LogMsg.return_register_section)
                loop_condition_register_page = False
        else:
            system("clear")
            print(tabulate(register_page, [Table.register_page.center(35)], tablefmt="heavy_grid"))
            print(f"Username: {input_username}")
            input_password = input("Password: ")
            try:
                Query_DB.register(input_username, input_password)
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
