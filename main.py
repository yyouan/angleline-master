import json
import os
import sys
import webbrowser
import time

##please "按照順序 cosole => login => choose => past => message => finish"
##lang:
'''
    python main.py --era console
    python main.py --era login
    python main.py --era check:angle
    python main.py --era check:head_url
    python main.py --era choose
    python main.py --era check:master
    python main.py --era past
    python main.py --era message
    python main.py --era finish

    if check has problem call them to re-login or --era choose again
'''

#interface variable
name=""  

#user interface
def main():
    if len(sys.argv) < 3: # 
        print("Usage:", sys.argv[0], "--era <test name>")
        sys.exit(1)       # 
    if sys.argv[1] != '--era': # 
        print("Usage:", sys.argv[0], "--era <test name>")
        sys.exit(1)       #
    global name
    name = sys.argv[2]
    

def write_package_json(filename):
    # Reading data back
    with open('package.json', 'r') as f:
        data = json.load(f)

    data["main"] = filename

    # Writing JSON data
    with open('package.json', 'w') as f:
        json.dump(data, f)

if(__name__ == "__main__"):
    main()
if name =="console":
    webbrowser.open_new_tab("https://dashboard.heroku.com/apps/angleline/logs")
    webbrowser.open_new_tab("https://dashboard.heroku.com/apps/angleline-master/logs")
    webbrowser.open_new_tab("https://dashboard.heroku.com/apps/angleline-hall/logs")
    webbrowser.open_new_tab("https://dashboard.heroku.com/apps/informationdesk/logs")
    print(os.system("git add ."))
    print(os.system("git commit -m \"ab\""))
    print(os.system("git config --global user.name \"yyouan\""))
    print(os.system("git pull https://github.com/yyouan/angleline-backup.git master")) 
    print(os.system("git pull https://github.com/yyouan/angleline.git master"))
    print(os.system("git pull https://github.com/yyouan/angleline-master.git master"))
    print(os.system("git pull https://github.com/yyouan/angleline-hall.git master"))
    print(os.system("git pull https://github.com/yyouan/informationdesk.git master"))
    print("please fix conflict problem in package.json") 
    print("please input:SELECT * FROM ACCOUNT; afer >>  (DELETE USE DELETE enter enter ;)")
    print(os.system("heroku pg:psql --app angleline < main.sql"))
    
elif name == "check:master":
    print(os.system("heroku pg:psql --app angleline < check_master.sql"))
elif name == "check:angle":
    print(os.system("heroku pg:psql --app angleline < check_angle.sql"))
elif name == "check:head_url":
    print(os.system("heroku pg:psql --app angleline < check_head_url.sql"))

elif name == "login":
    write_package_json("idle_angle.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline.git master"))
    time.sleep(5)
    write_package_json("idle_master.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-master.git master"))
    time.sleep(5)
    write_package_json("login.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-hall.git master"))
    time.sleep(5)
    write_package_json("info.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/informationdesk.git master"))
    time.sleep(5)
elif name == "choose":
    print(os.system("heroku pg:psql --app angleline < check_angle.sql"))
    print(os.system("heroku pg:psql --app angleline < check_head_url.sql"))    
    write_package_json("choose_master.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-hall.git master"))
    time.sleep(5)

elif name == "past":
    print(os.system("heroku pg:psql --app angleline < check_master.sql"))
    write_package_json("past_intro_angle.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline.git master"))
    time.sleep(5)
    write_package_json("past_intro_master.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-master.git master"))
    time.sleep(5)
    write_package_json("hall.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-hall.git master"))
    time.sleep(5)

elif name == "message":
    write_package_json("postman_angle.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline.git master"))
    time.sleep(5)
    write_package_json("postman_master.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-master.git master"))
    time.sleep(5)

elif name == "finish":
    write_package_json("exchange_id_angle.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline.git master"))
    time.sleep(5)
    write_package_json("exchange_id_master.js")
    print(os.system("git add ."))
    print(os.system("git commit -m \"login\""))
    print(os.system("git push https://github.com/yyouan/angleline-master.git master"))
    time.sleep(5)


