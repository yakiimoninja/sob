import sys
import os.path

# Checking if the osu! path is correct
def osu_path_check(path_param, default_path: bool):
    
    # Correcting the path if its missing ending slash
    path_param = slash_check(path_param)


    # Checks if the osu!.exe and "Songs" folder are present
    if os.path.exists(path_param + "osu!.exe") == True and os.path.exists(path_param + "Songs") == True:
        # Assigning variable for the Songs path
        path_param = path_param + "Songs"
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
    
    return path_param


# Checking if backup path is correct
def backup_path_check(path_param):

    # Correcting the path if its missing ending slash
    path_param = slash_check(path_param)

    print(path_param)

    # Checking if "osu!backup.json" exists in the path provided
    if "osu!backup.json" not in path_param:
        # If not slap it at the end of the path
        path_param = path_param + "osu!backup.json"

    # Checking if theres a slash after the files name and removes it
    if "osu!backup.json/" in path_param or "osu!backup.json\\" in path_param:
        path_param = path_param[:-1]


    # Checks if path exists
    if os.path.exists(path_param) == True:
        pass

    # Prompt if it does not exist
    else:
        print("\nNo osu!backup.json file found!\n\nPath provided is invalid!\n")
        sys.exit()
    
    return path_param

 
# Correcting the path if its missing ending slash
def slash_check(path_param):

    # For back slash
    if "\\" in path_param and "\\" != path_param[-1]:
        path_param = path_param + "\\"
        return path_param

    # For forward slash
    if "/" in path_param and "/" != path_param[-1]:
        path_param = path_param + "/"        
        return path_param

    return path_param