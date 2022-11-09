def get_int_from_user(prompt):
    user_input = input(prompt)
    n = int(user_input)
    return n

user_ipt = get_int_from_user('type an int: ')
print(f'int input: {user_ipt}')
