from watch_dog import main
from colorama import init, Fore, Style
import json

instructions = f"""
{Fore.GREEN}
Command List|    git => github operations; git -p => pull lastest changes
            |    mv => move files
            |
            |
{Style.RESET_ALL}
"""
invalid = f"""
{Fore.RED}
Command List|    git => github operations; git -p => pull lastest changes
            |    mv => move files
            |
            |
{Style.RESET_ALL}
"""

command_list = ['git', 'git -p', 'stop']


if __name__ == "__main__":

    print(instructions)
    while True:
        command  = input("Enter your command: ")

        # Command Validator

        if command not in command_list:
            print(invalid)
            break

        if command == 'git':
            main.git_service.git_push()
        if command == 'git -p': 
            main.git_service.git_pull()

        if command == 'stop':
            break
