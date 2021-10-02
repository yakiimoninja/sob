import requests
import json
import sys
import time


url = "https://osu.ppy.sh/home"
login_url = "https://osu.ppy.sh/session"

payload = {
    "username": "",
    "password": "",
    "_token": ""
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
    "Accept-Language": "en-US,en;q=0.5",
    "X-CSRF-Token": "",
    "Origin": "https://osu.ppy.sh",
    "Connection": "keep-alive",
    "Referer": "https://osu.ppy.sh/home"
}

download_headers = {
    "Connection": "keep-alive",
    "Referer": "https://osu.ppy.sh/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

def download_func(song_filename_list, song_link_list):

    # Getting credentials
    get_credentials()

    # Opening a request session
    with requests.Session() as s:

        # Getting the page source
        osu_html = s.get(url, headers= headers)
        osu_html = osu_html.text

        # Iterating through the page source to find the csrf-token
        for lines in osu_html.split("\n"):
            
            # Finding the token and writting it to the payload and header
            if 'name="_token" type="hidden" value="' in lines:
                payload["_token"] = lines[68:-2]
                headers["X-CSRF-Token"] = lines[68:-2]
                break
        

        # Making a login request
        login_request = s.post(login_url, data= payload, headers= headers)


        # Checking to see if login was succesful
        if login_request.status_code == 200:
            print("\n\nSuccesfully logged in!\n\n")
            pass
        
        if login_request.status_code <= 400 and login_request.status_code > 500 and login_request.status_code != 429:
            print("\nFailed to log in!\n\nCheck your credentials!\n")
            sys.exit()
        
        if login_request.status_code == 429:
            print("\nToo many requests!\n")
            sys.exit()


        # Iterating through the songs list
        for x in range(len(song_filename_list)):

            # Sending a download request
            download_request = s.get(song_link_list[x], headers= download_headers, stream=True)

            if download_request.status_code == 200:
                print(f"Downloading {x+1} out of {len(song_filename_list)} beatmaps!\n")
                pass
            else:
                print(f"Status Code: {download_request.status_code}!\n")
                sys.exit()

            
            # Writting the downloaded file to the songs folder
            with open ("osu!backup/songs/"+song_filename_list[x], "wb") as file:
                file.write(download_request.content)

            time.sleep(1)


def get_credentials():
    
    # Getting username from console
    payload["username"] = input("\nEnter your username: ").strip()
    
    # Checking for username validity
    if payload["username"] == "":
        print("\nEnter a valid username!\n")
        sys.exit()

    # Getting password from console
    payload["password"] = input("\nEnter your password: ").strip()

    # Checking for password validity
    if payload["password"] == "" and len(payload["password"]) < 8:
        print("\nEnter a valid password!\n")
        sys.exit()