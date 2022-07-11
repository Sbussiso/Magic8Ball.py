import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']


while True:

    shake = input('Press enter to shake: ')

    if shake =="":
        print(messages[random.randint(0,len(messages)-1)])

    else:
        print('invalid input')



