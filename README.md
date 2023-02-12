# Songs Osu! Backup (s.o.b.)

**Got a new computer and you want to migrate all your osu! beatmaps?\
No need to s.o.b. over having to manually do this.\
S.o.b. will back up and restore your songs for you.**

<img src="https://user-images.githubusercontent.com/80072600/137412880-10a1f486-801a-42cd-9b88-5223e2caff97.png" width="350" height="350" />

### Running the script file:
- You will need python 3.
- You will need to install the `requests` library.
- To install `requests` library execute: `python -m pip install requests`.
- After you've installed the requirements listed above, execute: `python sob.py`.

### Backing up:

 This will create a `osu!backup` folder in the same directory as the script.\
 Inside this folder you will find the `osu!backup.json` file containing all the song titles and their respective links.
  
### Restoring:

  You will need an osu! account.
  This will create a `songs` folder in the same directory as the script, containing all the downloaded `osz` beatmap files.
