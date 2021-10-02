import json
import os.path
import download


def restore(backup_file_path):

    song_filename_dict = []
    song_link_dict = []

    # Creating a songs backup folder if it doesnt exist
    if os.path.exists("osu!backup"):
        if os.path.exists("osu!backup/songs"):
            pass
        else:
            os.mkdir("osu!backup/songs")

    else:
        os.mkdir("osu!backup")
        os.mkdir("osu!backup/songs")


    with open(backup_file_path, "r") as backup_file:
        
        songs_json = json.load(backup_file)

        for x in range(len(songs_json)):

            song_filename_dict.append(songs_json[x]["File Name"])
            song_link_dict.append(songs_json[x]["Link"])
    
    download.download_func(song_filename_dict, song_link_dict)    
    
    print(f"\nDownloaded {len(song_filename_dict)} songs!\n") 
