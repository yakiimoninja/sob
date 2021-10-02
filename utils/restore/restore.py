import json
import utils.restore.download
from utils.folders import create_folder


def restore(backup_file_path):
    
    # This will create the backup folders needed
    create_folder(True)

    song_filename_list = []
    song_link_list = []

    # Opening the existing json file
    with open(backup_file_path, "r") as backup_file:
        
        songs_json = json.load(backup_file)

        for x in range(len(songs_json)):

            # Writting "File Name" and "Link" entries
            # from the file to seperate lists
            song_filename_list.append(songs_json[x]["File Name"])
            song_link_list.append(songs_json[x]["Link"])
    
    # Executing the download function on the song lists
    download.download_func(song_filename_list, song_link_list)    
    
    print(f"\nDownloaded {len(song_filename_list)} beatmaps!\n")