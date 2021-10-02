import sys
import os.path
from commands.backup.backup import backup
from commands.restore.restore import restore

help_message = "\nTo back-up your songs, execute              ->  python sob.py -b 'path_to_osu_folder'\nTo download your backed-up songs, execute   ->  python sob.py -r 'path_to_backup_file'\n"

song_list = [
    {
        "Title": "",
        "File Name": "",
        "Link": ""
    }
]


try:
    flag = sys.argv[1]
    flag = flag.strip()
    path_param = sys.argv[2]
    path_param = path_param.strip()


except IndexError:
    print("\nNo path provided!\n")


else:

    # Checks if the flag provided is valid
    if flag == "-b" or flag == "-r":
        pass
    else:
        print("\nWrong flag!\n" + help_message)
        sys.exit()


    # Checking for correct path format
    # Correcting the path if its missing backslash
    if "\\" not in path_param[-1]:
        path_param = path_param + "\\"



    # The back-up option.
    if flag == '-b':

        # Assigning separate path variables for the
        # osu!exe and the Songs path
        osu_exe_path = path_param + "osu!.exe"
        song_dir_path = path_param + "Songs"        
        
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