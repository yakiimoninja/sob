import sys
import os.path

# Checking if the osu! path is correct
def osu_path_check(path_param, default_path: bool):
    
    # Correcting the path if its missing backslash
    path_param = backslash_check(path_param)

    # Assigning separate path variables for the
    # osu!exe and the Songs path
    osu_exe_path = path_param + "osu!.exe"
    song_dir_path = path_param + "Songs"


    # Checks if the osu!.exe and "Songs" folder are present
    if os.path.exists(osu_exe_path) == True and os.path.exists(song_dir_path) == True:
        pass

    else:

        # Displaying different messages if osu! folder is not found
        if default_path == True:
            
            # If osu! is not found at the default location
            print("\nThe 'osu!' folder was not found at the default location!\n\nTry executing ->  python sob.py -b 'path_to_osu_folder'\n")
            sys.exit()
        
        else:
            # If the osu! path that was provided is wrong
            print("\nPath provided is invalid!\n")
            sys.exit()
    
    return song_dir_path


# Checking if backup path is correct
def backup_path_check(path_param):

    # Correcting the path if its missing backslash
    backslash_check(path_param)

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
        print("\nNo osu!backup.json file found!\n\nPath provided is invalid!\n")
        sys.exit()

 
# Correcting the path if its missing backslash
def backslash_check(path_param):

    if "\\" not in path_param[-1]:

        path_param = path_param + "\\"
        return path_param

    return path_param