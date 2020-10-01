
def enter_to_continue():
    while True:
        wait_for_user = input('Press enter to continue.\n')
        if wait_for_user == '':
            break


def user_input(prompt, before=None):
    '''
    prompt is displayed to user before they input anything, must be a string
    before is on the same line before the users input, must be a string
    '''
    # not unit testible, requires user input
    print(prompt, end='')
    if before:
        return input(before)
    return input()


def check_confirm(user_input):
    '''
    checks that the user has input y or n to confirm different things
    '''
    if not isinstance(user_input, str):
        raise TypeError(f'user_input needs to be a string not {type(user_input)}')

    import re
    if re.match('^[y]$', user_input, flags=re.IGNORECASE):
        return True
    elif re.match('^[n]$', user_input, flags=re.IGNORECASE):
        return False


def check_decimal(user_input):
    '''
    checks that user has entered a value that is a float
    '''
    if not isinstance(user_input, str):
        raise TypeError
    try:
        float(user_input)
    except ValueError:
        return False
    else:
        return True


def check_integer(user_input):
    '''
    checks that user has entered a value that is a integer
    '''
    if not isinstance(user_input, str):
        raise TypeError
    try:
        int(user_input)
    except ValueError:
        return False
    else:
        return True


def check_match(pattern, user_input):
    '''
    convenience to access re.match with ignorecase flag on
    takes a regex pattern and check that a users input matchs that regex pattern
    '''
    if not isinstance(pattern, str):
        raise TypeError
    if not isinstance(user_input, str):
        raise TypeError

    import re
    if not re.match(pattern, user_input, flags=re.IGNORECASE):
        return False
    
    return True


def check_text(user_input, spaces=False, symbols=None):
    '''
    symbols needs to be a string of characters to allow the user to enter
    '''
    if symbols and not isinstance(symbols, str):
        raise TypeError

    import re

    if spaces is True and symbols:
        pattern = r'^[a-zA-Z ' + symbols + ']$'
    elif symbols:
        pattern = r'^[a-zA-Z' + symbols + ']$'
    elif spaces is True:
        pattern = r'^[a-zA-Z ]$'
    else:
        pattern = r'^[a-zA-Z]$'

    for character in user_input:
        if not re.match(pattern, character):
            return False

    return True


def confirm(data_string):
    import re
    from resources.strings import confirm_text
    from utility.utility import add_newlines

    prompt = add_newlines(data_string) + confirm_text
    prompt = add_newlines(prompt)

    user_choice = user_input(prompt)
    while not re.match('^[yn]$', user_choice, flags=re.IGNORECASE):
        print('\nError, please enter Y for yes or N for no')
        user_choice = user_input(prompt)

    return check_confirm(user_choice)


def input_decimal(prompt, preced=None):
    decimal = user_input(prompt, preced)
    while not check_decimal(decimal):
        print('\nError, please enter a number value (base 10)')
        decimal = user_input(prompt, preced)
    
    return float(decimal)


def input_integer(prompt, preced=None):
    integer = user_input(prompt, preced)
    while not check_integer(integer):
        print('\nError, please enter a number value (base 10)')
        integer = user_input(prompt, preced)
    
    return integer


def input_text(prompt, spaces=False, symbols=None):
    if symbols and not isinstance(symbols, str):
        raise TypeError

    error_message = '\nError, please enter alpha characters'
    if spaces is True and symbols:
        error_message += f', spaces, or these {symbols}'
    elif spaces is True:
        error_message += ' or spaces'
    elif symbols:
        error_message += f' or these {symbols}'

    text = user_input(prompt)
    while not check_text(text, spaces, symbols):
        print(error_message)
        text = user_input(prompt)
    
    return text


class User_Input():
    def __init__(self, prompt):
        self.prompt = prompt

    # general
    def miles_traveled(self):
        from resources.strings import miles_traveled_succeed as succeed
        from utility.utility import prep_data_string

        miles_traveled = input_decimal(self.prompt)
        while not confirm(prep_data_string(miles_traveled, after=succeed)):
            miles_traveled = input_decimal(self.prompt)
        
        return miles_traveled

    def money(self, succeed=None):
        from resources.strings import money_symbol
        from utility.utility import prep_data_string

        money = input_decimal(self.prompt, money_symbol)
        while not confirm(prep_data_string(money, money_symbol, succeed)):
            money = input_decimal(self.prompt, money_symbol)

        return money

    # shift
    def fuel_economy(self):
        from resources.strings import fuel_economy_succeed
        from utility.utility import prep_data_string

        fuel_economy = input_decimal(self.prompt)
        while not confirm(prep_data_string(fuel_economy, after=fuel_economy_succeed)):
            fuel_economy = input_decimal(self.prompt)

        return fuel_economy
    
    def total_hours(self):
        from resources.strings import total_hours_succeed
        from utility.utility import prep_data_string

        total_hours = input_decimal(self.prompt)
        while not confirm(prep_data_string(total_hours, after=total_hours_succeed)):
            total_hours = input_decimal(self.prompt)
        
        return total_hours

    # delivery
    def average_speed(self):
        from resources.strings import average_speed_succeed
        from utility.utility import prep_data_string

        average_speed = input_integer(self.prompt)
        string = prep_data_string(average_speed, after=average_speed_succeed)
        while not confirm(string):
            average_speed = input_integer(self.prompt)

        return average_speed

    # order
    def id(self):
        from utility.utility import prep_data_string

        id = input_integer(self.prompt, '#')
        while not confirm(prep_data_string(id, 'Id is #')):
            id = input_integer(self.prompt, '#')

        return id

    # tip
    def card_tip(self):
        from resources.strings import card_tip_succeed as succeed
        return self.money(succeed)

    def cash_tip(self):
        from resources.strings import cash_tip_succeed as succeed
        return self.money(succeed)

    def unknown_tip(self):
        from resources.strings import unknown_tip_succeed as succeed
        return self.money(succeed)

    # extra stop
    def location(self):
        location = input_text(self.prompt, spaces=True, symbols=',./&?!:;()-+%')
        while not confirm(location):
            location = input_text(self.prompt, spaces=True, symbols=',./&?!:;()-+%')

        return location

    def reason(self):
        reason = input_text(self.prompt, spaces=True, symbols=',./&?!:;()-+%')
        while not confirm(reason):
            reason = input_text(self.prompt, spaces=True, symbols=',./&?!:;()-+%')

        return reason
