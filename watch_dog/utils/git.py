from os import system
from os import listdir
import time
import json

def handle_update(message, branch):
    system('git add .')
    system(f'git commit -m {message}')

    try:
         exit_code = system(f'git push origin {branch}')
         print(exit_code)
    except Exception as e:
        print(e)
        time.sleep(10)
        system(f'git push origin {branch}')

def handle_init(message, url, branch):

    system('git init')
    system('git add .')
    system(f'git commit -m {message}')
    system(f'git remote add origin {url}')

    try:
        system(f'git push origin {branch}')
    except Exception as e:
        time.sleep(10)
        system(f'git push origin {branch}')

def handle_pull(branch_name):
    with open('details.json', 'w') as json_file:
        json.dump({"branch" : branch_name}, json_file, indent=4)
    system(f'git pull origin {branch_name}')

class Git_service:

    def git_push(self):
        message = input("Enter your commit message: ")

        try: 
            with open('details.json', 'r') as json_file:
                loaded_data = json.load(json_file)
                branch = loaded_data['branch_name']

        except KeyError or json.decoder.JSONDecodeError:
            branch = False
        print(branch)
        
        files = listdir()

        if ".git" in files:
            handle_update(str(message), str(branch))
        else:
            print('Invalid')
        



    def git_pull(self):
        new_branch = input('Preferred branch name: ')
        message = input("Enter your commit message: ")

        handle_pull(new_branch)
        handle_update(message, new_branch)
