import os.path
import sys

help_message = "\nTo back-up your songs, execute              ->  python sob.py -b 'path_to_osu_folder'\nTo download your backed-up songs, execute   ->  python sob.py -r 'path_to_backup_file'\n"


def param_checks():
    # Getting console parameters
    
    flag = ""
    path_param = ""

    if len(sys.argv) == 2 and sys.argv[1].strip() == "-b":

        print("b option")
        flag = sys.argv[1].strip()
        path_param = os.path.expandvars(r"%LOCALAPPDATA%\osu!")


    
    elif len(sys.argv) == 3:
    
        flag = sys.argv[1]
        flag = flag.strip()
        print("2 params option")
        path_param = sys.argv[2]
        path_param = path_param.strip()
        

    elif len(sys.argv) == 2 and (sys.argv[1].strip() == "-h" or sys.argv[1].strip() == "?"):
        
        print(help_message)
    
    else:
        print("nothing")
    