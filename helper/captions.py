from enum import StrEnum


class Table(StrEnum):
    """
    This section belongs to the texts in the table
    """
    hm_page = "••• HANG MAN •••"
    main_page = "••• MAIN PAGE •••"
    ttt_page = "••• TIC TAC TOE •••"
    login_page = "••• LOGIN PAGE •••"
    description_hm = "[-hm] Hang Man"
    select_games = "••• SELECT GAMES •••"
    description_ttt = "[-ttt] Tic Tac Toe"
    safe_place = "You are in a safe place"
    register_page = "••• REGISTER PAGE •••"
    dad_page = "••• DUNGEON AND DRAGON •••"
    description_dad = "[-dad] Dungeon And Dragon"
    description_help = "[-help] About these games"
    description_easy = "[-easy] Easy level cost 4₵"
    description_hard = "[-hard] Hard level cost 22₵"
    dragon_smell = "!!! The dragon has smelled you !!!"
    description_normal = "[-normal] Normal level cost 10₵"
    description_register = "[-register] Create an account"
    description_login = "[-login] Already have an account"
    description_return = "[-return] Back to the previous page"
    dragon_hearing = "!!! The dragon heard your footsteps !!!"


class OtherMsg(StrEnum):
    """
    This is the rest of the text
    """
    clear = "clear"
    waiting = "Waiting"
    icon_input = ">>>  "
    username = "Username:"
    multi_games = "multi games"
    username_login = "You are login"
    valid_command = "Valid commands:"
    banned = "Sorry, you are banned :("
    input_valid = "Warning!!! Invalid input"
    dungeon_and_dragon = "dungeon and dragon"
    wrong_user_pass = "wrong username or password"
    congratulations = "\nCongratulations {}, you won {}₵"
    not_enough_coins = "Coins are not enough for this level\n"
    used_before_username = "Your username has been used before"
    successfully_registered = "You have successfully registered"
    input_ready = "if you are ready, press 'enter' on the keyboard"
    suggest_adv = "You can use '-adv' command to see ads to get 5₵"
    warning_rules_pw = "The password must be 8 to 12 characters long"
    warning_rules_user = "Username should start with an alphabetic letter"
    information_main_page = "Use the '-register' or '-login' command but if you need help,enter the '-help' command"
    information_before_run_dad = "{}, you lost {}₵ from your wallet, Now you have {}₵\n\nGAME GUIDE: You can only use 'up', 'down', 'left' and 'right'\n"


class LogMsg(StrEnum):
    """
    This section belongs to Logger texts
    """
    end = "end game"
    start = "start game"
    login = "'{}' login"
    registered = "'{}' registered"
    report_hint = "'{}' was shown a hint"
    duplicate_user = "'{}' Duplicate username"
    report_lose = "'{}' lost the game, wallet:'{}'"
    report_dragon = "Dragon Moved Position: '{}'"
    main_section = "The user is in the 'main' section"
    login_section = "The user is in the 'login' section"
    wrong_user_pw = "'{}' entered '{}' password incorrectly"
    register_section = "The user is in the 'register' section"
    adv_start_dad_section = "'{}' entered the '-adv', wallet:{}"
    report_levels = "'{}' is in the game on '{} level', wallet:{}"
    report_won = "'{}' won the game and received '{}' coins, wallet:'{}'"
    warning_rules_user = "The user did not follow the written rules"
    warning_rules_pw = "The user has not followed the password rules"
    select_games_section = "The user is in the 'select games' section"
    dad_section = "'{}' is in the 'dungeon and dragon' section, wallet:'{}'"
    report_levels_1 = "'{}' entered the '{}' and lost '{}' coins, wallet:'{}'"
    report_levels_2 = "'{}' entered the game with a counter of 1 2 3, wallet:'{}'"
    report_map = "Show map, Player position: '{}' The position of the dragon: {}"
    adv_end_dad_section = "'{}' ads ended and 5₵ were added to the wallet, wallet:'{}'"
    help_main_section = "The user entered the '-help' command in the 'main' section"
    exit_main_section = "The user entered the '-exit' command in the 'main' section"
    report_player = "Player position: '{}' and choose '{}' and current position is: '{}'"
    login_main_section = "The user entered the '-login' command in the 'main' section"
    return_login_section = "The user entered the '-return' command in the 'login' section"
    register_main_section = "The user entered the '-register' command in the 'main' section"
    return_dad_section = "'{}' entered the '-return' command in the 'dungeon and dragon' section"
    return_register_section = "The user entered the '-return' command in the 'register' section"
    command_report_main = "the user entered an unauthorized command >>> '{}' in the 'main' section"
    hm_select_games_section = "The user entered the '-hm' command in the 'select games' section"
    dad_select_games_section = "The user entered the '-dad' command in the 'select games' section"
    ttt_select_games_section = "The user entered the '-ttt' command in the 'select games' section"
    command_report_login = "the user entered an unauthorized command >>> '{}' in the 'login' section"
    command_report_register = "the user entered an unauthorized command >>> '{}' in the 'register' section"
    command_report_dad = "the user entered an unauthorized command >>> '{}' in the 'dungeon and dragon' section"
    command_report_select_games = "the user entered an unauthorized command >>> '{}' in the 'select games' section"
    logout_select_games_section = "'{}' entered the '-logout' command in the 'games' section and logged out, wallet:'{}'"


class DashMsg(StrEnum):
    """
    This section belongs to the command class
    """
    adv_8 = "why not"
    adv_9 = "thank you"
    adv_0 = "Hi, what are you doing here?"
    adv_4 = "Mapsa? What are you talking about?"
    adv_6 = "serious? Good, then I will go to register"
    adv_2 = "stop saying bullshits, What did you do with your money?"
    adv_3 = "I gave all the money I had to Mapsa for Django boot camp"
    exit = "Hope To See You Again...\n\nCopyright© 2023 Behdad Siavoshi"
    adv_1 = "Hello dude, I had come to play Dungeons and Dragons, but I didn't have enough money"
    adv_7 = "good luck, Just pay your money for the boot camp first, Can you please lend me 5 coins?"
    adv_5 = "A company in the field of oil and petrochemicals, but in one of its floors, programming is taught"
    help = """
    Hello, my friend

    You need an account to enter the game
    If you have, enter "-login" in the input field, otherwise,
    enter "-register" and create an account for yourself.
    And if you want to leave the game for any reason,
    use the '-exit' command and
    you can even go back to the previous page with '-return'
    Wherever you are in the program and you see the '>>>  ' icon,
    you can enter the desired command in it.
    Good luck





    This game created by
    Behdad Siavoshi
    In Jan 2023
    Version 1.0\n"""


if __name__ == "__main__":
    ...
