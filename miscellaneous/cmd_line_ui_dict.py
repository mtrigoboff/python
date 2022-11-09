import sys

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
        print(f'{cmd:6}{cmds[cmd][1]}')

def list_cmd():
    print('list command')

def quit_cmd():
    print('bye...')
    sys.exit()

# Python dictionary containing the legal commands and corresponding functions
help_cmd_list = [help_cmd,    'print list of commands']
cmds = {'a' : [append_cmd,  'append two files'],
        'h' : help_cmd_list,
        '?' : help_cmd_list,
        'd' : [delete_cmd,  'delete a file'],
        'l' : [list_cmd,    'print list of files'],
        'q' : [quit_cmd,    'quit app']}

# main loop
print('dictionary-based cmd line user interface')
while True:
    user_input = input('--> ')
    try:
        cmds[user_input][0]()
    except KeyError:
        print('unknown command:', user_input)
