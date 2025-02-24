from os import system
from os import listdir
import time
import json

def handle_update(message, branch):
    system('git add .')
    system(f'git commit -m {message}')

    try:
         system(f'git push origin {branch}')
    except Exception as e:
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
        # get commit message, get branch name
        message = input('Enter your commit message: ')
        try:
            with open('details.json', 'r') as old_branch:
                branch_file = json.load(old_branch)

                branch = branch_file['branch_name']

        except KeyError:
            branch = None
        except json.decoder.JSONDecodeError:
            branch = None

        files = listdir()
        if branch:
            print('sdf')

        if ".git" in files and branch:
            handle_update(message, branch)
            print('git push')

        else:

            new_branch = input('Preferred branch name: ')
            url = input("Enter branch url: ")
            data = {
                'branch_name' : str(new_branch)
            }

            with open('details.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            handle_init(message, url, new_branch)
            handle_update(message, new_branch)
            print('git pushed')

    def git_pull(self):
        new_branch = input('Preferred branch name: ')
        message = input("Enter your commit message: ")

        handle_pull(new_branch)
        handle_update(message, new_branch)
