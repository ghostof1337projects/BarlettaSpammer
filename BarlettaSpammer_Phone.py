#
#   ____            _____   _       ______  _______  _______           _____  _____          __  __  __  __  ______  _____  
#  |  _ \    /\    |  __ \ | |     |  ____||__   __||__   __| /\      / ____||  __ \  /\    |  \/  ||  \/  ||  ____||  __ \ 
#  | |_) |  /  \   | |__) || |     | |__      | |      | |   /  \    | (___  | |__) |/  \   | \  / || \  / || |__   | |__) |
#  |  _ <  / /\ \  |  _  / | |     |  __|     | |      | |  / /\ \    \___ \ |  ___// /\ \  | |\/| || |\/| ||  __|  |  _  / 
#  | |_) |/ ____ \ | | \ \ | |____ | |____    | |      | | / ____ \   ____) || |   / ____ \ | |  | || |  | || |____ | | \ \ 
#  |____//_/    \_\|_|  \_\|______||______|   |_|      |_|/_/    \_\ |_____/ |_|  /_/    \_\|_|  |_||_|  |_||______||_|  \_\
#                                                                                                                                                                                                                                                                                                                                                                       
#    _____   ____   _    _  _____    _____  ______    _____  ____   _____   ______                                          
#   / ____| / __ \ | |  | ||  __ \  / ____||  ____|  / ____|/ __ \ |  __ \ |  ____|                                         
#  | (___  | |  | || |  | || |__) || |     | |__    | |    | |  | || |  | || |__                                            
#   \___ \ | |  | || |  | ||  _  / | |     |  __|   | |    | |  | || |  | ||  __|                                           
#   ____) || |__| || |__| || | \ \ | |____ | |____  | |____| |__| || |__| || |____                                          
#  |_____/  \____/  \____/ |_|  \_\ \_____||______|  \_____|\____/ |_____/ |______|  
#                                  
#                                     @ghostof1337

import os
import platform
import socket
import sys
import time
import requests
import json
import threading

# version variable

__VERSION__ = '6.0'
group_name = 'BARLETTA SPAMMER ON TOP'
hostname = socket.gethostname()
os_name = platform.system()
architecture = platform.architecture()[0]
tick = "256"
TOKEN_FILE = "data.json"
CACHE = {}

def log(message):
     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
     log_message = f"[{timestamp}] {message}"
    
     with open("log.txt", "a", encoding="utf-8") as log_file:
         log_file.write(log_message + "\n")

def clear_log_file():
    file_path = "log.txt"
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)
    except IOError as e:
        print(f"Error: {e}")

clear_log_file()

log("INFO: BOOTING ...")
log("INFO: Initializing components...")
log("INFO: Checking for updates...")
log("INFO: Verifying system requirements...")
log("INFO: Connecting to the server...")
log("INFO: Authentication successful")
log("INFO: Starting background tasks...")
log("INFO: Application is ready")
log("INFO: Disabled window modification and maximize window")
log("INFO: Script started - The script has started executing.")
log("INFO: Setting up console - Configuring the console display for a welcoming interface.")
log("INFO: Checking if the token in token.json is valid...")
os.system("cls & mode 85,20 & title [Barletta Spammer] - Welcome")

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80), timeout=3)
        return True
    except OSError:
        return False

if not check_internet_connection():
    os.system('cls & mode 85,20 & title [Barletta Spammer] - NO INTERNET')
    log("ERROR: No internet connection established.")
    log("ERROR: Failed to ping www.google.com")
    log("FATAL ERROR: CHECK_INTERNET_CONNECTION_FAILED")
    print("\x1b[31m\n                           No internet connection. exiting...")
    time.sleep(4)
    sys.exit()

# Check if the "text.txt" file exists

if not os.path.exists("text.txt"): 

    message = "WARNING: text.txt COULD NOT BE FOUND, SO I CREATE ONE"
    print(message)
    log("WARNING: text.txt COULD NOT BE FOUND, SO I CREATE ONE")

    with open("text.txt", "w") as file:
        file.write("# :white_check_mark: This message was sent by BarlettaSpammer v6 | join gg/U3BfZCqCwJ to load :smiling_imp:\n")
        log("INFO: Custom message in text.txt added.")

# for status rage

STATUS_CONTENT = [
    "BARLETTASPAMMER ON TOP",
    "BARLETTASPAMMER STATUS CHANGER",
    "@ghostof1337 CREDIT",
    "YOU WILL DIE BITCH",
    "CRY",
    "I AM BETTER THAN YOU",
    "GO FUCK YOURSELF",
    "I'M UR FATHER",
    "NIGGA THINKS I'M USING BETTERDISCORD",
    "BARLETTASPAMMER.EXE",
    "ME >>> YOU",
    "U MAD?",
    "INJECTOR.EXE",
    "YOU HAVE NO CHOICE, FIGHT!",
    "UR WEAK HAHAHA",
    "UR FATHER IS GLIDING ON A SKATEBOARD",
    "LOUD NOISES",
    "SCREAMING IN TEXT",
    "NIGGA I CAUGHT U TRYNA BUST A LIP INTO A KID NIGGA",
    "MY NIGGA I CAUGHT U MASTURBATING TO CALL OUT MY NAME BY THE WEEKEND ON SLOWED AND REVERB NIGGA",
    "ABSOLUTE CHAOS",
    "UNSTOPPABLE FORCE",
    "YOU HAD A WHOLE CHICKEN COUP BUILT ON THE SIDES OF YO STOMACH, YOU FAT ASS NIGGA",
    "EXTREME SATAN",
    "TOTAL ANNIHILATION",
    "YOUR GRANDPA LIVES IN A GAY PRIDE ASYLUM",
    "DESTRUCTION INCARNATE",
    "APOCALYPSE HELL",
    "ENDLESS SCREAMING",
    "YOU CAN'T WIN AGAINST BARLETTA SPAMMER"
]

log("INFO: Pinging google.com")
log("INFO: Successfully loaded * STATUS_CONTENT = [] * list")

def get_username():
    if platform.system() == 'Windows':
        return os.getlogin()
    return os.environ.get('USER')

username = get_username()

# check is discord token if valid or not
def validate_discord_token(discord_token):
    try:
        headers = {
            'authorization': discord_token
        }
        response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
        response.raise_for_status()
        return True
    
    except requests.exceptions.RequestException as e:
        log(f"ERROR: {e}")
        return False

def validate_channel_id(discord_token, channelID):
    try:
        headers = {
            'authorization': discord_token
        }
        response = requests.get(f'https://discord.com/api/v10/channels/{channelID}', headers=headers)
        if response.status_code == 200:
            log("INFO: Validating channel ID - Validating the provided channel ID.")
            return True
        else:
            return False
        
    except requests.exceptions.RequestException as e:
        log(f"ERROR: {e}")
        return False

# token logic helped by: clixy, faby
def get_username(discord_token):
    if discord_token in CACHE:
        return CACHE[discord_token]

    try:
        headers = {
            'Authorization': discord_token
        }
        response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)

        if response.status_code == 200:
            user_info = response.json()
            CACHE[discord_token] = user_info['username']
            return user_info['username']
        else:
            return None
        
    except requests.RequestException as e:
        log(f"Request Exception: {e}")
        return None

def save_tokens_to_file(tokens):
    with open(TOKEN_FILE, "w") as token_file:
        token_data = {"tokens": tokens}
        json.dump(token_data, token_file)

def load_tokens_from_file():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as token_file:
            try:
                token_data = json.load(token_file)
                return token_data.get("tokens", [])
            except json.JSONDecodeError:
                pass
    return []

def validate_discord_token(token):
    return get_username(token) is not None

def select_account(tokens):
    valid_tokens_with_users = {}

    for token in tokens:
        username = get_username(token)
        if username:
            valid_tokens_with_users[token] = username

    if not valid_tokens_with_users:
        print("\x1b[31m\n                           No valid accounts found.")
        return None

    unique_usernames = list(valid_tokens_with_users.values())
    sorted_usernames = sorted(unique_usernames) # alphabetically
    unique_usernames = {username: idx for idx, username in enumerate(sorted_usernames, 1)}

    while True:
        os.system("cls & mode 80,25 & title [Barletta Spammer] - Loading Account...")
        print("\x1b[34m\n                           Loading Saved Accounts... \x1b[33m")
        log("INFO: Loading Saved Accounts...")
        time.sleep(1)

        os.system("cls & mode 80,25 & title [Barletta Spammer] - Select Account")
        print("\x1b[34m\n                           Available accounts: \n\x1b[33m")

        for idx, username in enumerate(unique_usernames, 1):
            print(f'\x1b[31m                           {idx}. \x1b[33m{username}')
            log(f"Loaded the following accounts:\n                           {idx}. {username}")

        try:
            choice = int(input("\x1b[34m\n                          Choose an account number: \x1b[33m"))

            if 1 <= choice <= len(sorted_usernames):
                selected_username = sorted_usernames[choice - 1]
                for token, username in valid_tokens_with_users.items():
                    if username == selected_username:
                        return token
            else:
                print('\x1b[31m\n                          Invalid input. Please choose a valid account number.')
                log("ERROR: Invalid input. Please choose a valid account number.")
                time.sleep(2)
                os.system("cls")

        except ValueError:
            print('\x1b[31m\n                          Invalid input. Please enter a number.')
            log("ERROR: Invalid input. Please enter a number.")
            time.sleep(2)
            os.system("cls")

def check_and_replace_invalid_tokens(tokens):
    updated_tokens = []
    invalid_tokens = {}

    for idx, token in enumerate(tokens, 1):
        if validate_discord_token(token):
            updated_tokens.append(token)
        else:
            invalid_tokens[token] = idx

    for token in invalid_tokens.keys():
        os.system(f"cls & mode 85,20 & title [BarlettaSpammer] - Invalid token")
        print(f"\x1b[31m\n                           Token number {invalid_tokens[token]} is invalid.")
        log(f"WARNING: token number {invalid_tokens[token]} is invalid.")
        time.sleep(2)

        while True:
            replace = input(f"\x1b[34m\n                           Do you want to replace the token {invalid_tokens[token]}? (yes, YES, Y, y / no, NO, N, n.): \x1b[33m").lower()
            if replace in ['yes', 'y', 'YES', 'Y']:
                new_token = input(f"\x1b[34m\n                           TOKEN ({invalid_tokens[token]}): \x1b[33m")

                while not validate_discord_token(new_token):
                    print("\x1b[31m\n                           Invalid token. Please enter a valid Discord token.")
                    log("WARNING: Invalid token. Please enter a valid Discord token.")
                    time.sleep(2)
                    os.system("cls")
                    new_token = input(f"\x1b[34m\n                           TOKEN ({invalid_tokens[token]}): \x1b[33m")

                if new_token in tokens or new_token in updated_tokens:
                    print("\x1b[31m\n                           Tokens are the same or already exists. Please enter another token.")
                    log("WARNING: This token is already in use.")
                    continue

                updated_tokens.append(new_token)
                break

            elif replace in ['no', 'n', 'NO', 'N']:
                updated_tokens.append(token)
                break

            else:
                print("\x1b[31m\n                           Invalid input. Please enter yes, y or no, n.")
                log("WARNING: Invalid input.")
                time.sleep(2)
                os.system("cls")

    with open("data.json", "w") as token_file:
        token_data = {"tokens": updated_tokens}
        json.dump(token_data, token_file)

    return updated_tokens

tokens_to_check = load_tokens_from_file()
tokens_to_check = check_and_replace_invalid_tokens(tokens_to_check)
save_tokens_to_file(tokens_to_check)

while len(tokens_to_check) < 20:
    if len(tokens_to_check) == 0:
        new_token = input(f'\x1b[34m\n                           TOKEN: \x1b[33m')

    elif len(tokens_to_check) == 1 or len(tokens_to_check) == 2 or len(tokens_to_check) == 3 or len (tokens_to_check) == 4 or len (tokens_to_check) == 5 or len (tokens_to_check) == 6 or len (tokens_to_check) == 7 or len (tokens_to_check) == 8 or len (tokens_to_check) == 9 or len (tokens_to_check) == 10 or len (tokens_to_check) == 11 or len (tokens_to_check) == 12 or len (tokens_to_check) == 13 or len (tokens_to_check) == 14 or len (tokens_to_check) == 15 or len (tokens_to_check) == 16 or len (tokens_to_check) == 17 or len (tokens_to_check) == 18 or len (tokens_to_check) == 19:
        add_more = input(f"\x1b[34m\n                           Do you want to add another token ({len(tokens_to_check) + 1})? (yes, YES, Y, y / no, NO, N, n.): \x1b[33m").lower()
        log("INFO: Asking token.")

        if add_more in ['no', 'n', 'NO', 'N']:
            break

        elif add_more in ['yes', 'y', 'YES', 'Y']:
            new_token = input(f'\x1b[34m\n                           TOKEN {len(tokens_to_check) + 1}: \x1b[33m')
            log(f"INFO: Adding token {len(tokens_to_check) + 1}")
            time.sleep(2)
            os.system("cls")

        else:
            print("\x1b[31m\n                           Invalid input. Please enter (yes, YES, Y, y / no, NO, N, n.)")
            log("WARNING: Invalid input. Please enter (yes,YES, Y, y / no, NO, N, n.).")
            continue

    while not validate_discord_token(new_token):
        print("\x1b[31m\n                           Invalid token. Please enter a valid Discord token.")
        log("WARNING: Invalid token.")
        new_token = input(f'\x1b[34m\n                           TOKEN {len(tokens_to_check) + 1}: \x1b[33m')

    if new_token in tokens_to_check:
        print("\x1b[31m\n                           Tokens are the same!")
        log("WARNING: The following tokens are the same.")
        continue

    tokens_to_check.append(new_token)
    save_tokens_to_file(tokens_to_check)

selected_token = select_account(tokens_to_check)

if selected_token:
    discord_token = selected_token

def get_discord_username(discord_token):
    try:
        headers = {
            'authorization': discord_token
        }
        response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
        response.raise_for_status()
        user_data = response.json()
        return user_data['username']
    except requests.exceptions.RequestException as e:
        log(f'\x1b[31m\n                                FAILED TO FETCH DISCORD USERNAME\n{e}')
        return None

discord_username = get_discord_username(discord_token)

def invalidate_token(discord_token):
    logout_url = 'https://discord.com/api/v10/auth/logout'
    headers = {
        'authorization': discord_token
    }
    response = requests.post(logout_url, headers=headers)
    if response.status_code == 204:
        log("INFO: Token invalidated successfully - The provided token has been invalidated.")
        print(f"\x1b[34m\n                           Succesfully invalidated the token: {discord_token}")
        time.sleep(2)
        sys.exit(1)
    else:
        log("ERROR: Failed to invalidate token - Invalidating the provided token failed.")
        print("\x1b[31m\n                           Failed to invalidate the token.")

while True:
    invalidate_choice = input(f"\x1b[34m\n                          Do you want to RESET the token with the account \x1b[36m[{discord_username}]\x1b[34m ? (yes, YES, Y, y / no, NO, N, n.): \x1b[33m").lower()

    if invalidate_choice in ["yes", "y", "YES", "Y"]:
        print("Resetting token...")
        time.sleep(2)
        invalidate_token(discord_token)

    elif invalidate_choice in ["no", "n", "NO", "N"]:
        print("\x1b[31m\n                                Task Cancelled. No token has been reset.")
        time.sleep(1)
        os.system("cls")
        break

    else:
        print("\x1b[31m\n                                Please enter a valid option. yes, YES, Y, y or no, NO, N, n.")
        time.sleep(2)
        os.system("cls")

def status_rage(discord_token, status_message):
    headers = {
        'authorization': discord_token,
    }
    data = {
        'custom_status': {
            'text': status_message
        }
    }
    response = requests.patch('https://discord.com/api/v10/users/@me/settings', headers=headers, json=data)
    
    if response.status_code == 200:
        log(f"INFO: Successfully changed status to: {status_message}")
    else:
        log("ERROR: Failed to change status.")


def status_change_thread():
    while True:
        for status_message in STATUS_CONTENT:
            status_rage(discord_token, status_message)
            time.sleep(10)

status_thread = threading.Thread(target=status_change_thread)


while True:
    status_rage_choice = input("\x1b[34m\n                           Do you want to turn on status changer? [every 10 seconds] (yes, YES, Y, y / no, NO, N, n.): \x1b[33m").lower()
    if status_rage_choice in ["yes", "y", "YES", "Y"]:
        status_thread.start()
        break
    elif status_rage_choice in ["no", "n", "NO", "N"]:
        print("\x1b[34m\n                           Continuing the script without changing the status.\n")
        log("INFO: Script continues without changing the status.")
        break
    else:
        print("\x1b[31m\n                           Please enter a valid option. yes, YES, Y, y or no, NO, N, n.")

log("INFO: Fetching Discord username - Fetching the username associated with the provided token.")
log("INFO: Discord username retrieved - Discord username successfully retrieved.")
log("INFO: Retrieving system information - Gathering information about the system platform and setup.")
log("INFO: System information retrieved - Successfully retrieved system information.")
os.system("cls")

channelID = None
while not channelID:
    channelID = input('\x1b[34m\n                           Enter the channel ID: \x1b[33m')
    log("REQUEST: Asking for channel ID")
    
    if not validate_channel_id(discord_token, channelID):
        print('\x1b[31m\n                           INVALID CHANNEL ID.')
        time.sleep(2)
        os.system("cls")
        log("ERROR: Invalid channel ID. Please provide a valid channel ID.")
        channelID = None

def change_group_name(discord_token, group_id):
    headers = {
        'Authorization': discord_token,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'name': f'{group_name}'
    }

    requests.patch(f'https://discord.com/api/v10/channels/{group_id}', headers=headers, json=payload)

while True:
    choice = input("\x1b[32m\n\n                           1. Spam\n                           2. Afk check (100s) [NEW!]\n\x1b[34m\n\n                           Enter your choice: \x1b[31m")

    try:
        choice = int(choice)
        if choice != 1 and choice != 2:
            print("\x1b[31m\n                           Invalid input. Please select 1 or 2.")
            time.sleep(2)
            os.system("cls")
            continue

    except ValueError:
        print("\x1b[31m\n                           Invalid input. Please select 1 or 2.")
        time.sleep(2)
        os.system("cls")
        continue

    log("INFO: Requesting channel ID - Prompting the user to input the Discord channel ID.")
    log("INFO: Successfully received the Discord API.")
    log("INFO: Starting...")
    print('\x1b[34m\n                                Connecting...\n')
    time.sleep(0.5)
    print('\x1b[34m\n                           Fetching Discord API...\n')
    time.sleep(0.4)
    print('\x1b[1;37m       ACCOUNT  :\x1b[1;32m ' + discord_username)
    print('\x1b[1;37m       HOSTNAME :\x1b[1;32m ' + hostname)
    print('\x1b[1;37m       OS       :\x1b[1;32m ' + os_name)
    print('\x1b[1;37m       ARCH     :\x1b[1;32m ' + architecture)
    print('\x1b[1;37m       TICK     :\x1b[1;32m ' + tick)
    print('\x1b[31m\n\n               \n                    ╔╗ ┌─┐┬─┐┬  ┌─┐┌┬┐┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐\n                    ╠╩╗├─┤├┬┘│  ├┤  │  │ ├─┤  ╚═╗├─┘├─┤││││││├┤ ├┬┘\n                    ╚═╝┴ ┴┴└─┴─┘└─┘ ┴  ┴ ┴ ┴  ╚═╝┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─\n               \n               ')
    print(f'''\n                              \x1b[1;37m{username}\x1b[31m@\x1b[1;32m{hostname}\n\n               \n \x1b[1;34m''')
    
    log("INFO: Successfully connected to Discord.")

    if choice == 1:
    
        headers = {
            'Authorization': discord_token,
        }

        message_count = 0

        while True:
            with open("text.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            for line in lines:
                try:
                    response = requests.post(
                        f"https://discord.com/api/v10/channels/{channelID}/messages",
                        headers=headers,
                        json={"content": line.strip()}
                    )

                    if response.status_code == 200:
                        message_count += 1
                        message_count_str = f"Messages sent successfully: {message_count}"
                        print(f"\r\x1b[34m{message_count_str}", end='', flush=True)

                    if response.status_code == 403:
                        log("WARNING: No permission to send messages.")

                    if response.status_code == 404:
                        log("WARNING: Channel not found.")

                    if response.status_code == 429:
                        retry_after = response.json().get('retry_after')
                        time.sleep(retry_after)

                    if response.status_code == 502: 
                        log("WARNING: Bad Gateway.")

                except requests.exceptions.RequestException as e:
                    log(f"WARNING: {e} | Retrying every 20 seconds...")
                    time.sleep(20)
                    log("WARNING: Retrying...")
                    continue

    if choice == 2:

        headers = {
            'Authorization': discord_token,
        }

        afk_check_count = 0

    try:
        response = requests.post(
            f"https://discord.com/api/v10/channels/{channelID}/messages",
            headers=headers,
            json={"content": "# AFK CHECK STARTED, IF YOU DON'T RESPOND UNTIL I REACH UP TO 100 YOU LOSE! | BarlettaSpammer Afk Checker"}
        )

        while afk_check_count < 100:

            response = requests.post(
                f"https://discord.com/api/v10/channels/{channelID}/messages",
                headers=headers,
                json={"content": str(afk_check_count + 1)}
            )

            if response.status_code == 200:
                afk_check_count += 1
                afk_check_count_str = f"Messages sent successfully: {afk_check_count}"
                print(f"\r\x1b[34m{afk_check_count_str}", end='', flush=True)

            if afk_check_count == 100:
                time.sleep(1)
                os.system("cls")

            if response.status_code == 403:
                log("WARNING: No permission to send messages.")

            if response.status_code == 404:
                log("WARNING: Channel not found.")

            if response.status_code == 429:
                retry_after = response.json().get('retry_after')
                time.sleep(retry_after)

            if response.status_code == 502:
                log("WARNING: Bad Gateway")

    except requests.exceptions.RequestException as e:
            log(f"\nWARNING: {e} | Retrying every 20 seconds...")
            time.sleep(20)
            log("WARNING: Retrying...")
            continue