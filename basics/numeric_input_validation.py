def get_int_from_user(prompt):
    user_input = input(prompt)
    try:
        n = int(user_input)
        return True, n
    except ValueError:
        return False, user_input

valid_ipt, user_ipt = get_int_from_user('type an int: ')
if valid_ipt:
    print(f'valid int input: {user_ipt}')
else:
    print(f'invalid int input: \'{user_ipt}\'')