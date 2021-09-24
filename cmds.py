import json
import os.path

def backup(song_list, song_dir_path):

    # Getting the names of each folder, since its the same as the song name
    folder_list = [item for item in os.listdir(song_dir_path) if os.path.isdir(os.path.join(song_dir_path, item)) ]


    # Iterating the list of folder names
    for x in range(len(folder_list)):

        if folder_list[x] != "Failed":
            song_number = ""
            song_title = ""
            song_link = ""
            space_counter = 0

            # Creating new list entries
            if x > 0:
                song_list.append({
                    "Title": "",
                    "Link": "",
                    "No Video": False
                })           
            
            # Iterating the letters in each line
            for y in range(len(folder_list[x])):
                
                # When it spots the first space in the title, does the following
                if folder_list[x][y] == " " and space_counter == 0:
                    
                    # Formatting to remove the preceding numbers based on 
                    # the position of the first space we found
                    # and setting a new title without the numbers        
                    song_title = folder_list[x]
                    song_title = song_title[y+1:]
                    song_list[x]["Title"] = song_title  # (to be json)

                    # Formatting the following string to produce 
                    # the numbers used in the link
                    # eg. https://osu.ppy.sh/beatmapsets/999645
                    song_number = folder_list[x]
                    song_number = song_number[:y]

                    # This is to helps to determine the first space in the line
                    space_counter += 1

            # Checking the value of "No Video" to format the title and link accordingly
            if "[no video]" in folder_list[x]:

                # Setting the "No Video" to True in list (to be json)
                song_list[x]["No Video"] = True

                # Formatting the string to remove the "no video"
                # and setting it as the new title
                song_title = song_title[:-11]
                song_list[x]["Title"] = song_title  # (to be json)

                # Contructing the link of the song
                song_link = "https://osu.ppy.sh/beatmapsets/" + song_number + "/download?noVideo=1"

            else:
                song_link = "https://osu.ppy.sh/beatmapsets/" + song_number + "/download"
            
            # Setting the link in the songs list (to be json)
            song_list[x]["Link"] = song_link

        # Opening and writing the backup in a json file            
        with open("osu_backup.json", "w") as output:
            json.dump(song_list, output, ensure_ascii=False, indent= 4)
    
    print(f"\nSuccesfully backed up {len(song_list)} songs!")