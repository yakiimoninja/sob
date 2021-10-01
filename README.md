# Songs Osu! Backup (s.o.b.)
> #### A python script that backs up your osu! songs.
#
**Got a new computer and you want to migrate all your osu! songs?\
No need to s.o.b. over having to manually do this. (pun intended :wink:)\
sob" python script will back up and restore your songs for you.**

## Usage

**_Restoring songs will require an osu! account._**

- **Backing up:**
  - Navigate in the directory the python script is located.
  - Execute the script with the `-b` flag, followed by the osu! folder path.
  - `python sob.py -b "C:\Example\Location\osu!"`

  This will create a `osu_backup.json` file in the same directory as the script, containing all the song titles and their respective links.
  
- **Restoring:**
  - Navigate in the directory the python script is located.
  - Execute the script with the `-r` flag, followed by the `osu_backup.json` path.
  - `python sob.py -r "C:\Example\Location\osu_backup.json"`
  - You will be promted to provide your account credentials.
  
  This will create a `songs` folder in the same directory as the script, containing all the downloaded `.osz` files.
