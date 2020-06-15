from os import path, remove

from input_data import get_input, input_data
from utility import enter_to_continue, now, read_data, to_datetime, write_data


class Split:
    def __init__(self, parent):
        # list of all paths
        self.path = parent.path
        self.miles_path = path.join(self.path, 'split_miles_traveled.txt')
        self.start_time_path = path.join(self.path, 'split_start_time.txt')
        self.end_time_path = path.join(self.path, 'split_end_time.txt')
        self.info_path = path.join(self.path, 'split_info.txt')

    # methods for split tracking
    def consolidate(self):
        self.save()
        # remove files that are no longer needed
        remove(self.miles_path)
        remove(self.start_time_path)
        remove(self.end_time_path)

    def end(self):
        self.start_time = to_datetime(read_data(self.start_time_path))
        while True:
            user_check = get_input(
                'Are you sure you want to end the split?\n'
                'Y: yes\n'
                'N: no\n', str)
            if user_check in ('y', 'Y'):
                self.start_time = to_datetime(read_data(self.start_time_path))
                if path.exists(self.miles_path):
                    self.miles_traveled = float(read_data(self.miles_path))
                else:
                    self.input_miles_traveled()
                if path.exists(self.end_time_path):
                    self.end_time = to_datetime(read_data(self.end_time_path))
                else:
                    self.end_time = now()
                    write_data(self.end_time_path, self.end_time)
                self.consolidate()
                return self
            elif user_check in ('n', 'N'):
                exit()
            else:
                print('\nInvalid input...')

    def load(self):
        split_info = read_data(self.info_path).split(',')
        self.miles_traveled = split_info[0]
        self.start_time = split_info[1]
        self.end_time = split_info[2]
        return self

    def save(self):
        write_data(self.info_path, self.string())

    def start(self):
        while True:
            user_check = get_input(
                'Are you sure you want to start a split?\n'
                'Y: yes\n'
                'N: no\n', str)
            if user_check in ('y', 'Y'):
                write_data(self.start_time_path, now())
                enter_to_continue()
                exit()
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    # methods for inputting data
    def input_miles_traveled(self):
        self.miles_traveled = input_data(
            '\nTotal miles traveled for split:\t#.#\n', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), word=' miles')
        write_data(self.miles_path, self.miles_traveled)

    # utility methods
    def string(self):
        return f'{self.miles_traveled},{self.start_time},{self.end_time}'