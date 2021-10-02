import sys
import os.path
from utils.backup import backup
from utils.restore.restore import restore
from utils.args.args import args_checks


# Song list format that will translated to a json
song_list = [
    {
        "Title": "",
        "File Name": "",
        "Link": ""
    }
]

flag = ""
path_param = ""

# Checks the validity of the arguments
flag, path_param = args_checks()

# Correctly formats the path

# Checks if paths are correct


# The back-up option.
if flag == "-b":

    # Executing the backup function containing all the logic
    backup(song_list, song_dir_path)


# The restore option
if flag == "-r":

    # Executing the restoration function containing all the logic
    restore(osu_backup_path)
    

print("\nExitting.\n")