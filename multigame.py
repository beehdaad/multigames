import logging
from os import system
import logging.config
from time import sleep

import cowsay
from stringcolor import cs
from tabulate import tabulate

from accounts import (
    login,
    register,
    DataBase,
    AllowedWord,
    PasswordRange,
)
from helper import (
    Table,
    LogMsg,
    command,
    OtherMsg,
    LoadingLogo,
    LoadingIcon,
    LoadingCountNum,
)
from games.dungeon_and_dragon import (
    DrawMap,
    LevelHard,
    LevelEasy,
    MoveDragon,
    HintDungeon,
    LevelNormal,
    MoveCharacter,
    AllowedDirection,
)

"""
The implementation of the program is from this part, which was written by nested loop
"""

logging.config.fileConfig(fname='log/log_setting.toml', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger_dad = logging.getLogger("dad")

USER_INFORMATION = dict()
INTERNAL_DATABASE = list()


logger.info(LogMsg.start)
DataBase.check_existence_file()
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
    INTERNAL_DATABASE = DataBase.read_file()
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
                if input_username[0] == "-":
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
                        user_account = register(input_username, input_password)
                    except AllowedWord:
                        logger.info(LogMsg.warning_rules_user)
                        print(OtherMsg.warning_rules_user)
                        sleep(0.7)
                    except PasswordRange:
                        logger.info(LogMsg.warning_rules_pw)
                        print(OtherMsg.warning_rules_pw)
                        sleep(0.7)
                    else:
                        content = user_account.register(INTERNAL_DATABASE)
                        if content is True:
                            logger.info(LogMsg.registered.format(input_username))
                            LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                            print(OtherMsg.successfully_registered)
                            sleep(0.7)
                            loop_condition_register_page = False
                        else:
                            logger.info(LogMsg.duplicate_user.format(input_username))
                            print(OtherMsg.used_before_username)
                            sleep(0.7)
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
                if input_username[0] == "-":
                    try:
                        user_command = command(input_username, ("-return",))
                    except ValueError:
                        logger.info(LogMsg.command_report_login.format(input_username))
                        print(OtherMsg.valid_command, "'-return'")
                        sleep(0.7)
                    else:
                        logger.info(LogMsg.return_login_section)
                        loop_condition_login_page = False
                elif input_username[0].isalpha():
                    system("clear")
                    print(tabulate(login_page, [Table.login_page.center(35)], tablefmt="heavy_grid"))
                    print(f"{OtherMsg.username} {input_username}")
                    input_password = input("Password: ")
                    user_account = login(input_username, input_password)
                    USER_INFORMATION, content = user_account.login(INTERNAL_DATABASE)
                    if content is True:
                        logger.info(LogMsg.login.format(input_username))
                        LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                        print(OtherMsg.username_login)
                        sleep(0.7)
                        wallet = int(USER_INFORMATION["wallet"])
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
                            print(f"Hi, {USER_INFORMATION['username']}")
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
                                    logger.info(LogMsg.logout_select_games_section.format(USER_INFORMATION["username"], wallet))
                                    LoadingIcon(OtherMsg.waiting, 0.2, 3).show()
                                    user_account.logout(INTERNAL_DATABASE, USER_INFORMATION)
                                    USER_INFORMATION.clear()
                                    loop_condition_select_games = False
                                    loop_condition_login_page = False
                                    INTERNAL_DATABASE = DataBase.read_file()
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
                                    # -------------------------DUNGEON ADN DRAGON-------------------------
                                    loop_condition_dad_page = True
                                    while loop_condition_dad_page:
                                        system("clear")
                                        logger.info(LogMsg.dad_section.format({USER_INFORMATION['username']}, wallet))
                                        select_levels = [
                                                        [Table.description_easy],
                                                        [Table.description_normal],
                                                        [Table.description_hard]
                                                        ]
                                        print(f"{USER_INFORMATION['username']}, you have {wallet}₵")
                                        print(tabulate(select_levels, [Table.dad_page.center(35)], tablefmt="heavy_grid"))
                                        input_command = input(OtherMsg.icon_input).casefold()
                                        try:
                                            user_command = command(input_command, ("-easy", "-normal", "-hard", "-adv", "-return"))
                                        except ValueError:
                                            logger.info(LogMsg.command_report_dad.format({USER_INFORMATION['username']}))
                                            print(OtherMsg.valid_command, "'-easy' '-normal' '-hard' '-adv' '-return'")
                                            sleep(0.7)
                                            system("clear")
                                        else:
                                            levels = {"-easy": (4, 7), "-normal": (10, 16), "-hard": (22, 40)}
                                            if input_command == "-adv":
                                                logger.info(LogMsg.adv_start_dad_section.format({USER_INFORMATION['username']}, wallet))
                                                coin = user_command.dash_adv(1.3)
                                                wallet += coin
                                                USER_INFORMATION.update(wallet=wallet)
                                                logger.info(LogMsg.adv_end_dad_section.format(USER_INFORMATION['username'], wallet))
                                            elif input_command == "-return":
                                                loop_condition_dad_page = False
                                                logger.info(LogMsg.return_dad_section.format(USER_INFORMATION['username']))
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
                                                    USER_INFORMATION.update(wallet=wallet)
                                                    logger.info(LogMsg.report_levels_1.format(USER_INFORMATION["username"], input_command, levels[input_command][0], wallet))
                                                    print(OtherMsg.information_before_run_dad.format(USER_INFORMATION['username'], levels[input_command][0], wallet))
                                                    input(OtherMsg.input_ready)
                                                    logger.info(LogMsg.report_levels_2.format(USER_INFORMATION["username"], wallet))
                                                    LoadingCountNum(0.9)
                                                    # -------------------------PLAY GAME DUNGEON AND DRAGON-------------------------
                                                    if input_command == "-easy":
                                                        value = LevelEasy()
                                                    elif input_command == "-normal":
                                                        value = LevelNormal()
                                                    elif input_command == "-hard":
                                                        value = LevelHard()
                                                    logger_dad.info(LogMsg.report_levels.format(USER_INFORMATION['username'], input_command.lstrip("-"), wallet))
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
                                                        logger_dad.info(LogMsg.report_map.format(value.player, value.dragon))
                                                        direction = AllowedDirection.check(value.table_size, value.player, value.wall)
                                                        move = input(f"{direction} : ").casefold()
                                                        if move in direction:
                                                            value.player = MoveCharacter(value.player, move).perform()
                                                            logger_dad.info(LogMsg.report_player.format(draw_map.player, move, value.player))
                                                            draw_map.player = value.player
                                                            if not input_command == "-easy":
                                                                alarm = MoveDragon.distance(value)
                                                                if isinstance(alarm, int):
                                                                    value.dragon, alarm = MoveDragon.perform(value, alarm)
                                                                    logger_dad.info(LogMsg.report_dragon.format(value.dragon))
                                                        if value.player == value.dragon:
                                                            system("clear")
                                                            cowsay.dragon("YOU LOSE!")
                                                            loop_condition_dad_game = False
                                                            logger_dad.info(LogMsg.report_lose.format(USER_INFORMATION['username'], wallet))
                                                            sleep(2)
                                                        elif value.player == value.dungeon:
                                                            system("clear")
                                                            cowsay.cow("YOU WON!")
                                                            print(cs(OtherMsg.congratulations.format(USER_INFORMATION['username'], levels[input_command][1]), "green"))
                                                            loop_condition_dad_game = False
                                                            wallet += levels[input_command][1]
                                                            USER_INFORMATION.update(wallet=wallet)
                                                            logger_dad.info(LogMsg.report_won.format(USER_INFORMATION['username'], levels[input_command][1], wallet))
                                                            sleep(2)
                                                        elif value.player == value.hint and input_command != "-easy":
                                                            draw_map.hint = None
                                                            value.hint = None
                                                            system("clear")
                                                            input("Please unmute your speaker\nPress 'enter' and listen carefully ")
                                                            # Tested with Mac OS
                                                            # If you get an error, comment the bottom line
                                                            HintDungeon.play(value.dungeon)
                                                            logger_dad.info(LogMsg.report_hint.format(USER_INFORMATION['username']))
                    else:
                        logger.info(LogMsg.wrong_user_pw.format(input_username, input_password))
                        print(OtherMsg.wrong_user_pass)
                        sleep(0.7)
                else:
                    logger.info(LogMsg.command_report_main.format(input_command))
                    print(OtherMsg.input_valid)
                    sleep(0.7)
logger.info(LogMsg.end)
if __name__ == "__main__":
    ...
