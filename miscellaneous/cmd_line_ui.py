# main loop
while True:
    user_input = input('--> ')
    if user_input == 'q':
        print('bye...')
        break
    elif user_input == 'a':
        print('append command')
    elif user_input == 'd':
        print('delete command')
        file_name = input('file name --> ')
        confirm = input('are you sure (y or n)? --> ')
        if confirm == 'y':
            print(f'deleting {file_name}')
            # write code to actually delete file
        else:
            print('delete canceled')
    elif user_input == 'l':
        print('list command')
    else:
        print('illegal command:', user_input)