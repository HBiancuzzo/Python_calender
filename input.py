import os


def input_field(instructions):
    ins = ''
    while ins == '':
        statement = input('Ins: ')
        for i in range(len(instructions.split(']')) - 1):
            if statement.upper() == instructions.split(']')[i][-1]:
                ins = statement.upper()
    return ins


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
