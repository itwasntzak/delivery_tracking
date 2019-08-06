import datetime
import os
import shutil

import shift


def now():
    return datetime.datetime.now()


def deliveryNumb(option):
    if option == 'number':
        with open(os.path.join("deliveryTracking", "deliveryNumb.txt"), 'r') as dlvNumb:
            return dlvNumb.read()

    elif option == 'update':
        with open(os.path.join("deliveryTracking", "deliveryNumb.txt"), 'r+') as dlvNumb:
            prevDlvNumb = int(dlvNumb.read())
            dlvNumb.seek(0)
            dlvNumb.write(str(prevDlvNumb + 1))

    elif option == 'reset':
        with open(os.path.join("deliveryTracking", "deliveryNumb.txt"), 'w') as dlvNumb:
            dlvNumb.write('0')

    elif option == 'change':
        while True:
            print('\nALERT!!!\nare you sure you want to change the delivery number?\n1 for yes | 2 for no')
            try:
                userInput = int(input())
                if userInput == 1:
                    print('\nwhat is the new current delivery number:')
                    try:
                        changeDeliveryNumb = int(input())
                        with open(os.path.join("deliveryTracking", "deliveryNumb.txt"), 'w') as dlvNumb:
                            dlvNumb.write(str(changeDeliveryNumb))
                            break

                    except ValueError:
                        print('\ninvalid input...')

                elif userInput == 2:
                    break

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


def beginOrdNumb(option):
   if option == 'number':
      with open(os.path.join("deliveryTracking", 'beginOrdNumb.txt'), 'r') as first3:
         return first3.read()

   elif option == 'change':
      while True:
          print('\nALERT!!!\nare you sure you want to change the order number preset?\n1 for yes | 2 for no')
          try:
              userInput = int(input())
              if userInput == 1:
                  print('\nwhat is the new set of 3 numbers for order number preset:')
                  first3Numbs = input()
                  with open(os.path.join("deliveryTracking", "beginOrdNumb.txt"), 'w') as first3:
                      first3.write(str(first3Numbs))
                  return first3Numbs

              elif userInput == 2:
                  break

          except ValueError:
              print('\ninvalid input...')

          else:
              print('\ninvalid input...')


def overWriteCheck():
    if os.path.exists(os.path.join("shift")) == True:
        while True:
            print("\nALERT!!!\nare you sure you want to overwrite today's file?\n1 for yes | 2 for no")
            try:
                userInput = int(input())
                if userInput == 1:
                    shutil.rmtree(os.path.join("shift"))
                    shift.startShift()
                    break

                elif userInput == 2:
                    break

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')

    else:
        return print("\nALERT!!!\nfile doesn't exist")

def timeTook(startTime, endTime, varWord):
    timeDif = endTime - startTime
    mins = int(timeDif.total_seconds() / 60)
    secs = timeDif.total_seconds() - (mins * 60)

    if mins == 0:
        print('\nit took you ' + str(secs) + ' seconds to complete this ' + varWord)

    elif mins == 1:
        print('\nit took you ' + str(mins) + ' minute and ' + str(secs) + ' seconds to complete this ' + varWord)

    elif mins > 1:
        print('\nit took you ' + str(mins) + ' minutes and ' + str(secs) + ' seconds to complete this ' + varWord)

    elif mins >= 60:
        print('\nit took you more then an hour to complete this order')


def areYouSure(option):
    while True:
        print('\n' + option + ' is this correct?\n1 for yes | 2 for no')
        try:
            areYouSure = int(input())
            if areYouSure == 1:
                return True

            elif areYouSure == 2:
                return False

        except ValueError:
            print('\ninvalid input...')

        else:
            print('\ninvalid input...')


def writeData(folder, folder1, file, data, back=''):
    with open(os.path.join(folder, folder1, file), 'w') as fileObject:
        fileObject.write(str(data))

    if back == 'back':
        return data

    else:
        pass