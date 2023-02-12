import os.path

is_path_correct: bool 

# Checking if the osu! path is correct
def osu_path_check(path_param, default_path: bool):
    
    # Setting default location
    if default_path == True:
        path_param = os.path.expandvars(r"%LOCALAPPDATA%\osu!")

    # Correcting the path if its missing ending slash
    path_param = slash_check(path_param)


    # Checks if the osu!.exe and "Songs" folder are present
    if os.path.exists(path_param + "osu!.exe") == True and os.path.exists(path_param + "Songs") == True:
        # Assigning variable for the Songs path
        path_param = path_param + "Songs"
        is_path_correct = True

    else:
        # Displaying different messages if osu! folder is not found
        if default_path == True:
            # If osu! is not found at the default location
            print("\nThe 'osu!' folder was not found at the default location!")
            is_path_correct = False
        
        # If the osu! path that was provided is wrong
        else:
            print("\nPath provided is invalid!")
            is_path_correct = False
    
    
    return path_param, is_path_correct


# Checking if backup path is correct
def backup_path_check(path_param, default_path: bool):

    # Setting default location
    if default_path == True:
        path_param = "osu!backup/"

    # Correcting the path if its missing ending slash
    path_param = slash_check(path_param)

    # Checking if "osu!backup.json" exists in the path provided
    if "osu!backup.json" not in path_param:
        # If not slap it at the end of the path
        path_param = path_param + "osu!backup.json"

    # Checking if theres a slash after the files name and removes it
    if "osu!backup.json/" in path_param or "osu!backup.json\\" in path_param:
        path_param = path_param[:-1]



    # Checks if path and file exist
    if os.path.exists(path_param) == True:
        is_path_correct = True

    # Prompt if they do not exist
    else:

        # If its backup folder/file arent in the default location
        if default_path == True:
            print("\nThe osu!backup.json file is not found at the default location!")
            is_path_correct = False

        # If the path to the backup folder is false
        else:
            print("\nPath provided is invalid!\nNo osu!backup.json file found!")
            is_path_correct = False
    
    return path_param, is_path_correct

 
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