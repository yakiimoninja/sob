import sys
import os.path
from utils.backup import backup
from utils.restore.restore import restore
from utils.args.args import args_get


# Song list format that will translated to a json
song_list = [
    {
        "Title": "",
        "File Name": "",
        "Link": ""
    }
]


# Checks for correct console input
# Formats the console input
# Passes the formated input to the variables below
flag, path_param = args_get()


# The back-up option.
if flag == "-b":

    # Executing the backup function containing all the logic
    # Requires the song [list] and the path to the songs directory
    backup(song_list, path_param)


# The restore option
if flag == "-r":

    # Executing the restoration function containing all the logic
    # Requires the path to the backup directory
    restore(path_param)

print("\nExitting.\n")