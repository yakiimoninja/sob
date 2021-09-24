import sys
import os.path

help_message = "\nTo back-up your songs, execute              ->  python sob.py -e 'path_to_osu_folder'\nTo download your backed-up songs, execute   ->  python sob.py -i 'path_to_backup_file'\n"

songs_list = [
    {
        "Title": "",
        "Link": "",
        "No Video": True
    }
]

try:
    flag = sys.argv[1]
    flag = flag.strip()
    path_param = sys.argv[2]
    path_param = path_param.strip()

    # Checks if the flag provided is valid
    if flag == "-e" or flag == "-i":
        pass
    else:
        print("\nWrong flag!\n" + help_message)
        sys.exit()

    # The back-up option.
    if flag == '-e':

        # Checking for correct path format
        # Correcting the path if its missing backslash
        if "\\" not in path_param[-1]:
            path_param = path_param + "\\"

        # Assigning separate path variables for the
        # osu!exe and the Songs path
        osu_exe_path = path_param + "osu!.exe"
        songs_dir_path = path_param + "Songs"        
        
        # Checks if this is the osu! folder
        if os.path.exists(osu_exe_path) == True and os.path.exists(songs_dir_path) == True:
            pass 
        else:
            print("\nCheck your path again!\nThis isn't the osu! folder!\n")
            sys.exit()
        
        # Getting the names of each folder, since its the same as the song name
        folders_list = [item for item in os.listdir(songs_dir_path) if os.path.isdir(os.path.join(songs_dir_path, item)) ]
        print(folders_list[1])

        # Iterating the list of folder names
        for x in range(len(folders_list)):
            
            song_title = ""
            song_link = ""
            space_counter = 0

            # Checking to see if there is a "no video" string in the title
            if "[no video]" in folders_list[x]:

                # Setting the "No Video" to True in list (to be json)
                songs_list[0]["No Video"] = True

                # Formatting the string to remove the "no video"
                # and setting it as the new title
                song_title = folders_list[x]
                songs_list[0]["Title"] = song_title[:-11]
            
            # Iterating the letters in each line
            for y in range(len(folders_list[x])):
                
                # When it spots the first space in the title, does the following
                if folders_list[x][y] == " " and space_counter == 0:
                    
                    # Formatting to remove the preceding numbers based on 
                    # the position of the first space we found
                    # and setting a new title without the numbers
                    song_title = folders_list[x]
                    songs_list[0]["Title"] = song_title[y+1:]
                    
                    # Formatting the following string to produce 
                    # the link of the actual beatmap which
                    # needs the numbers we took out of the title
                    # eg. https://osu.ppy.sh/beatmapsets/999645
                    song_link = folders_list[x]
                    song_link = song_link[:y]
                    song_link = "https://osu.ppy.sh/beatmapsets/" + song_link
                    # Setting the link in the songs list (to be json)
                    songs_list[0]["Link"] = song_link
                    
                    # This is to determine the first space in the line
                    space_counter += 1


        print(songs_list)

    # The import option
    #if flag == '-i':
    
    print("Done!")


except IndexError:
    print("\nNo path provided!\n")