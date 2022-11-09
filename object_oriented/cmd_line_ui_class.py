import sys

class Command:
    def __init__(self, cmd_fn, cmd_description):
        self.cmd_fn = cmd_fn
        self.cmd_description = cmd_description

def append_cmd():
    print('append command')

def delete_cmd():
    print('delete command')
    file_name = input('file name --> ')
    confirm = input('are you sure (y or n)? --> ')
    if confirm == 'y':
        print(f'deleting file {file_name}')
        # write code to actually delete file here
    else:
        print(f'delete file {file_name} canceled')

def help_cmd():
    print('cmd   description')
    for cmd in sorted(cmds):
        print(f'{cmd:6}{cmds[cmd].cmd_description}')

def list_cmd():
    print('list command')

def quit_cmd():
    print('bye...')
    sys.exit()

# Python dictionary containing the legal commands and corresponding functions
help_cmd_list = [help_cmd,    'print list of commands']
cmds = {'a' : Command(append_cmd,  'append two files'),
        'h' : Command(*help_cmd_list),
        '?' : Command(*help_cmd_list),
        'd' : Command(delete_cmd,  'delete a file'),
        'l' : Command(list_cmd,    'print list of files'),
        'q' : Command(quit_cmd,    'quit app')}

# main loop
print('dictionary and class-based cmd line user interface')
while True:
    user_input = input('--> ')
    try:
        cmds[user_input].cmd_fn()
    except KeyError:
        print('unknown command:', user_input)
