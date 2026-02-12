from pyscript import display, document

def signup(e):
    document.getElementById('passwordnotice').innerHTML = ''

    username = document.getElementById('usernameen').value
    password = document.getElementById('passworden').value

    if len(username)>=86:
        display(f'Your username must have at least 8 characters.', target="passwordnotice")

    if password.isalpha():
        display(f'Your password needs 2 more numbers.', target='passwordnotice')

    elif password.isdigit():
        display(f'You password must have at least 8 letters.', target='passwordnotice')

    elif len(password)<= 8:
        display(f'Your password is too short, it must have at least 8 characters.', target='passwordnotice')

    else:
        display(f'Account has been created. You may enter.', target='passwordnotice')


