import sys
import os.path
from utils.backup import backup
from utils.restore import restore
from utils.params import param_checks


# Song list format that will translated to a json
song_list = [
    {
        "Title": "",
        "File Name": "",
        "Link": ""
    }
]


try:

    flag, path_param = param_checks()

except IndexError:
    print("\nNo path provided!\n")


else:


    # The back-up option.
    if flag == '-b':

        # Assigning separate path variables for the
        # osu!exe and the Songs path
        osu_exe_path = path_param + "osu!.exe"
        song_dir_path = path_param + "Songs"        
        
        print(osu_exe_path, song_dir_path)
        # Checks if the osu!.exe and "Songs" folder is present
        if os.path.exists(osu_exe_path) == True and os.path.exists(song_dir_path) == True:
            pass 
        else:
            print("\nThis isn't the osu folder!\nCheck your path again!\n")
            sys.exit()

        # Executing the backup function containing all the logic
        backup(song_list, song_dir_path)



    # The restore option
    if flag == "-r":

        # Assigning path variable for the 
        # location of the backup file
        osu_backup_path = path_param

        # Checking validity of path and formatting accordingly
        if "osu!backup.json" not in path_param:
            osu_backup_path = path_param + "osu!backup.json"
        if "osu!backup.json" in path_param:
            osu_backup_path = osu_backup_path[:-1]

        # Prompt for bad path
        if os.path.exists(osu_backup_path) == True:
            pass 
        else:
            print("\nNo osu!backup.json file found!\nCheck your path again!\n")
            sys.exit()

        # Executing the restoration function containing all the logic
        restore(osu_backup_path)
        

    print("\nExitting.\n")