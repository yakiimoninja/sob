import os.path


def create_folder(make_songs_folder: bool):

    if make_songs_folder == True:
        # Creating a songs backup folder if it doesnt exist
        if os.path.exists("osu!backup"):
            if os.path.exists("osu!backup/songs"):
                pass
            else:
                os.mkdir("osu!backup/songs")
        else:
            os.mkdir("osu!backup")
            os.mkdir("osu!backup/songs")
            
    else:
        # Creating the backup folder if it doesnt exist
        if os.path.exists("osu!backup"):
            pass
        else:
            os.mkdir("osu!backup")