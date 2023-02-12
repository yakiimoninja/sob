import requests
import time
import concurrent.futures


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

def download(song_filename_list, song_link_list):

    song_filename_list = song_filename_list
    song_link_list = song_link_list

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

            print("\nSuccesfully authenticated!")
            print(f"Status code: {login_request.status_code}\n")

            # Time measuring
            start_time = time.time()

            # Multi threading
            for i in range(len(song_filename_list)):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(get_file, song_filename_list, song_link_list, i, s)

            # Time measuring
            end_time = time.time()
            formatted_time = "{:.1f}".format(end_time - start_time)
            
            # Ending print
            print(f"\nFinished downloading {len(song_filename_list)} beatmaps in {formatted_time} second(s)!")
            
        
        if login_request.status_code >= 400 and login_request.status_code < 500 and login_request.status_code != 429:
            print("\nFailed to authenticate!")
            print(f"Status code: {login_request.status_code}")
            
        
        if login_request.status_code == 429:
            print("\nToo many requests!")
            print(f"Status code: {login_request.status_code}")
    


# Getting the beatmap file (called by the thread pool executor)
def get_file(song_filename_list, song_link_list, i, s):

    # Sending a download request
    download_request = s.get(song_link_list[i], headers= download_headers, stream=True)

    # If download is succesful 
    if download_request.status_code == 200:
        print(f"Downloading {i+1} out of {len(song_filename_list)} beatmaps!")

        # Writting the downloaded file to the songs folder
        with open ("osu!backup/songs/"+ song_filename_list[i], "wb") as file:
            file.write(download_request.content)

    # If download request isnt succesful
    else:
        print("\nFailed to download!")
        print(f"Status code: {download_request.status_code}")


# Getting credentials
def get_credentials():

    # Getting username from console
    payload["username"] = input("\nEnter your username: ").strip()
    
    # Checking for username validity
    while payload["username"] == "":
        print("\nEnter a valid username!\n")
        payload["username"] = input("Enter your username: ").strip()

    # Getting password from console
    payload["password"] = input("Enter your password: ").strip()

    # Checking for password validity
    while payload["password"] == "" and len(payload["password"]) < 8:
        print("\nEnter a valid password!\n")
        payload["password"] = input("Enter your password: ").strip()