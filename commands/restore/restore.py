import json
from commands.restore.download import download_func
from commands.folders import create_folder


def restore(backup_file_path):

    song_filename_list = []
    song_link_list = []

    # This will create the backup folders needed
    create_folder(True)

    with open(backup_file_path, "r") as backup_file:
        
        songs_json = json.load(backup_file)

        for x in range(len(songs_json)):

            song_filename_list.append(songs_json[x]["File Name"])
            song_link_list.append(songs_json[x]["Link"])
    
    download_func(song_filename_list, song_link_list)    
    
    print(f"\nDownloaded {len(song_filename_list)} beatmaps!\n")