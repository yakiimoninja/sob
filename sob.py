import sys
from utils import path_check
from utils.backup import backup
from utils.restore.restore import restore


help_message = "\n- To back up all your beatmaps: Press 'b'.\n- To restore all your beatmaps: Press 'r'.\n\n- To exit: Press 'x'.\n"

# Song list format that will translated to a json
song_list = [
    {
        "Title": "",
        "File Name": "",
        "Link": ""
    }
]

print("\n==========================================")
print("\n\t     Welcome to sob!")
print("\n==========================================")
print(help_message)
flag = input("> ").strip()

# Checking for flag validity
while not ((flag == "b" or flag == "r" or flag == "x") and flag != ""):

    print("\nWrong flag!\n", help_message)
    flag = input("> ").strip()


# Looping the main menu
while True:

    # The backup option
    if flag == "b":
        
        # Checking for default path validity
        path_param = ""
        path_param, is_path_correct = path_check.osu_path_check(path_param, default_path=True)

        # Checking for provided path validity
        while is_path_correct != True:
            print("Please provide the full path to the 'osu!' folder.\n")
            path_param = input("> ").strip()
            path_param, is_path_correct = path_check.osu_path_check(path_param, default_path=False)

        # Executing the backup
        backup(song_list, path_param)


    # The restore option
    if flag == "r":
        
        # Checking for default path validity
        path_param = ""
        path_param, is_path_correct = path_check.backup_path_check(path_param, default_path=True)

        # Checking for provided path validity
        while is_path_correct != True:
        
            print("Please provide the full path to the 'osu!backup' folder.\n")
            path_param = input("> ").strip()
            path_param, is_path_correct = path_check.backup_path_check(path_param, default_path=False)

        # Executing the restoration
        restore(path_param)


    # The exit option
    if flag == "x":
        sys.exit()


    print(help_message)
    flag = input("> ").strip()
