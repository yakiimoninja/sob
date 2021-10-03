import os.path
import sys
from utils.args import path_check

help_message = "\n\nTo back up:\nIf osu! is installed at the default location      ->  python sob.py -b\nIf osu! isn't installed at the default location   ->  python sob.py -b 'path_to_osu_folder'\n\nTo restore:\nTo download all your backed-up songs, execute     ->  python sob.py -r 'path_to_backup_file'\n"


def args_get():

    # For cases of 1 received console argument
    if len(sys.argv) == 2:
        
        # If its the "-b" flag
        if sys.argv[1].strip() == "-b":

            # We give the default osu! install location
            flag = sys.argv[1].strip()
            path_param = os.path.expandvars(r"%LOCALAPPDATA%\osu!")
        
            # Checks if osu! folder is in the deafult path
            path_param = path_check.osu_path_check(path_param, default_path=True)

        # If its the "-h" or "?" flag
        elif sys.argv[1].strip() == "-h" or sys.argv[1].strip() == "?":
            print(help_message)
        
        # If its the "-r" flag
        elif sys.argv[1].strip() == "-r":
            print("\nNo path provided!\n", help_message)
        
        # Anything else
        else:
            print("\nInvalid flag provided!\n", help_message)
    
    # For cases of 2 received console argument
    elif len(sys.argv) == 3:
    
        # Assigning variables to the console arguments
        flag = sys.argv[1]
        flag = flag.strip()
        path_param = sys.argv[2]
        path_param = path_param.strip()

        # For the "-r" flag
        if flag == "-r":
            # Checks if osu! folder is in the path provided
            path_param = path_check.backup_path_check(path_param)
        
        # For the "-b" flag
        elif flag == "-b":
            # Checks if osu! folder is in the path provided
            path_param = path_check.osu_path_check(path_param, default_path=False)
        
        # Anything else
        else:
            print(path_param)
            print("\nInvalid flag provided!\n", help_message)
        
    # For more than 2 console arguments
    else:
        print("\nInvalid flag provided!\n", help_message)

    return flag, path_param