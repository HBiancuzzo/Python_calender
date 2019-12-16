from function import Calendar
from display import Ui, display_event_group, display_create_event
from valid import date_valid, time_valid, number_valid, span_valid
from input import input_field, clean_screen

default_month = '1'
default_day = '1'
display = 'Month'
start_input = False
ce_array = ['', '', '', '']

while True:
    clean_screen()
    Ui.say_month(default_month)

    if display == 'Month':
        Ui.display_month(default_month)
    elif display == 'Event':
        display_event_group(default_month, 'Month')
    elif display == 'Create':
        display_create_event(ce_array[0], ce_array[1], ce_array[2], ce_array[3])
    elif display == 'Day':
        display_event_group(default_month, 'Day', default_day)

    #

    if not display == 'Create':
        Ui.say_instructions(Ui.instructions)
        ins_input = input_field(Ui.instructions)
    else:
        Ui.say_instructions(Ui.instructions_ce)
        ins_input = 'C'
        start_input = True

    #

    if ins_input == 'Q':  # Quit
        break

    elif ins_input == 'M':  # Month
        if display == 'Month':
            ins_input = input('Choose the month(1-12): ')
            while not number_valid(ins_input, 0, 12):
                ins_input = input('Choose the month(1-12): ')
            default_month = str(ins_input)
        display = 'Month'

    elif ins_input == 'E':  # Events of the month
        display = 'Event'

    elif ins_input == 'L':  # Left
        if default_month == '1':
            default_month = '12'
        else:
            default_month = str(int(default_month) - 1)

        if not display == 'Month' and not display == 'Event':
            display = 'Month'

    elif ins_input == 'R':  # Right
        if default_month == '12':
            default_month = '1'
        else:
            default_month = str(int(default_month) + 1)

        if not display == 'Month' and not display == 'Event':
            display = 'Month'

    elif ins_input == 'C':  # Create event
        display = 'Create'
        if start_input:
            ins_input = input_field(Ui.instructions_ce)
            if ins_input == 'C':
                for i in range(4):
                    if ce_array[i] == '':
                        ins_input = Ui.instructions_ce.split(']')[i+2][-1]
                        break
                cal = Calendar(ce_array[0], ce_array[1], int(ce_array[3]))
                if not cal.save_to_calendar(ce_array[2]):
                    print('Sorry that time is occupied')
                    input('Enter to continue')
                else:
                    display = 'Month'
                    ins_input = 'M'
                    start_input = False
            if ins_input == 'E':
                display = 'Month'
                ins_input = 'M'
                start_input = False
            elif ins_input == 'D':
                date = input('Date (Month/Day): ')
                while not date_valid(date):
                    date = input('Date (Month/Day): ')
                ce_array[0] = date
            elif ins_input == 'T':
                title = input('Title: ')
                ce_array[2] = title
            elif ins_input == 'S':
                if ce_array[1] == '':
                    ins_input = 'H'
                else:
                    span = input('Span (Number): ')
                    while not span_valid(span, ce_array[1]):
                        span = input('Span (Number): ')
                    ce_array[3] = span
            if ins_input == 'H':
                hour = input('Hour (Hour:Minute): ')
                while not time_valid(hour):
                    hour = input('Hour (Hour:Minute): ')
                ce_array[1] = hour

    elif ins_input == 'D':
        default_day = input('Choose what day you want to see: ')
        while not date_valid(f'{default_month}/{default_day}'):
            default_day = input('Choose what day you want to see: ')
        display = 'Day'
