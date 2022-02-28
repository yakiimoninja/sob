# Songs Osu! Backup (s.o.b.)

**Got a new computer and you want to migrate all your osu! beatmaps?\
No need to s.o.b. over having to manually do this.\
S.o.b. will back up and restore your songs for you.**

<img src="https://user-images.githubusercontent.com/80072600/137412880-10a1f486-801a-42cd-9b88-5223e2caff97.png" width="350" height="350" />


## Requirements

### To use the restoration functionality you will need an osu! account!

### If you using the executable file:
- You will only need an osu! account (if you plan to restore).

### If you are running the script file:
- You will need an osu! account (if you plan to restore).
- You will need python 3.
- You will need to install the `requests` library.
- To install `requests` library execute: `python -m pip install requests`

- ### If you want to build from source:
  - Install python 3.
  - Install `requests` library with: `python -m pip install requests`.
  - Install `pyinstaller` with: `python -m pip install pyinstaller`.
  - Build an `exe` with: `pyinstaller sob.py --clean -F`.


## Usage

### Exe file:
  
  You can get the `exe` from the [releases](https://github.com/yakiimoninja/sob/releases/latest) tab.
  
  Execute the `sob.exe` and you'll be prompted with remaining instructions there.
  
  If `sob.exe` doesn't seem to start you might need to unblock it.\
  `Right click -> Properties -> Unblock -> Apply`
  
  If you are worried about the antivirus and virustotal flags you shouldn't be, these are false positives.\
  But don't take my word for it, inspect the code yourself and build an `exe` with `pyinstaller` if you want.\
  See above "***If you want to build from source***".
  
### Script file:

  After you've installed the requirements listed above, execute: `python sob.py`

### Backing up:

 This will create a `osu!backup` folder in the same directory as the script.\
 Inside this folder you will find the `osu!backup.json` file containing all the song titles and their respective links.
  
### Restoring:

  You ***will*** be promted to provide your account credentials.\
  This will create a `songs` folder in the same directory as the script, containing all the downloaded `osz` beatmap files.
