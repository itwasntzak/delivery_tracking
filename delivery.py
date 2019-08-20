import os

import util_func
import order
import input_data


def on_delivery(prompt, start_time):
    # creating file so code knows while on delivery, and continue
    with open(os.path.join('delivery', 'on_delivery'), 'w'):
        pass

    while True:
        print('\n' + prompt + '\n1 after returning | 2 for extra stop')
        try:
            wait_for_user = int(input())
            if wait_for_user == 1:
                os.remove(os.path.join('delivery', 'on_delivery'))
                break
            elif wait_for_user == 2:
                extra_stop(start_time=start_time)
                continue
        except ValueError:
            print('\ninvalid input')
        else:
            print('\ninvalid input')


def extra_stop(start_time):
    # creating file so code knows while on extra stop, to be able to continue
    with open(file=os.path.join('delivery', 'extra_stop'), mode='w'):
        pass

    while True:
        print('\nMaking extra stop...\n1 to continue')
        try:
            wait_for_user = int(input())
            if wait_for_user == 1:

                # input extra stop name and save it
                extra_stop_name = input_data.input_data(
                    prompt1='\nName of extra stop:\n', input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n', input_type2=str, option_yes='y', option_no='n')
                util_func.write_data(path='delivery', file=extra_stop_name + '_extra_stop.txt', data=str(extra_stop_name))

                # input extra stop reason and creating a file with that as contents
                util_func.write_data(
                    path='delivery', file=extra_stop_name + '_reason.txt', data=input_data.input_data(
                        prompt1='\nReason for extra stop?\n', input_type1=str,
                        prompt2='\nIs this correct? [y/n]\n', input_type2=str, option_yes='y', option_no='n'))

                # input and saving miles traveled
                miles_trav(var_path='extra')

                # save the time at the end of the extra stop
                extra_end_time = util_func.write_data(path='delivery', file=extra_stop_name + '_end_time.txt', data=util_func.now(), back=True)

                util_func.time_took(start_time=start_time, end_time=extra_end_time, var_word='extra stop')
                os.remove(path=os.path.join('delivery', 'extra_stop'))
                return

        except ValueError:
            print('\nInvalid input...')
        else:
            print('\nInvalid input...')


def miles_trav(var_path, var_word=''):
    miles_trav_input = input_data.input_data(
        prompt1='\n' + var_word + 'miles traveled:\n', input_type1=float,
        prompt2='\nIs this correct? [y/n]\n', input_type2=str, option_yes='y', option_no='n')
    util_func.write_data(path='delivery', file=str(var_path) + '_miles_trav.txt', data=miles_trav_input)


def numb_of_orders():
    return util_func.write_data(
        path='delivery', file='numbOfOrders.txt', data=input_data.input_data(
            prompt1='\nNumber of orders?\n', input_type1=int,
            prompt2='\nIs this correct? [y/n]\n', input_type2=str, option_yes='y', option_no='n'),
        back=True)


def delivery():
    os.mkdir(path=os.path.join(path='delivery'))
    start_time = util_func.write_data(path='delivery', file='delivery_start_time.txt', data=util_func.now(), back=True)
    number_of_orders = numb_of_orders()

    if number_of_orders == 1:
        on_delivery(prompt='\nDriving to address...', start_time=start_time)

        order_number = order.order_number()

        order.tip(var_path=order_number)

        miles_trav(var_path=order_number)

        order_end_time = util_func.write_data(path='delivery', file=str(order_number) + '_end_time.txt', data=util_func.now(), back=True)

        util_func.time_took(start_time=start_time, end_time=order_end_time, var_word='order')


    elif number_of_orders >= 1:
        for value in range(number_of_orders):
            on_delivery(prompt='\nDriving to address...', start_time=start_time)

            order_number = order.order_number()

            order.tip(var_path=order_number)

            miles_trav(var_path=order_number)

            order_end_time = util_func.write_data(path='delivery', file=str(order_number) + '_end_time.txt', data=util_func.now(), back=True)

            util_func.time_took(start_time=start_time, end_time=order_end_time, var_word='order')

    on_delivery(prompt='Driving back to store...', start_time=start_time)

    miles_trav(var_path='total', var_word='total ')

    delivery_end_time = util_func.write_data(path='delivery', file='delivery_end_time.txt', data=util_func.now(), back=True)

    util_func.time_took(start_time=start_time, end_time=delivery_end_time, var_word='delivery')

    util_func.write_data(path='shift', file='number_of_deliveries.txt', data=int(util_func.delivery_number('number')) + 1)