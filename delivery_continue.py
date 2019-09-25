#//TODO: still needs to be written
#//TODO: still needs to be refactored


import os
import shutil
import datetime

import utility_function
import delivery
import order


def deliveryContinue():
    if os.path.exists(os.path.join('delivery')):
        if os.path.exists(os.path.join('delivery', 'deliveryStartTime.txt')) == False:
            shutil.rmtree(os.path.join('delivery'))

        else:
            if os.path.exists(os.path.join('delivery', 'onDelivery')) == True and os.path.exists(os.path.join('delivery', 'extraStop')) == True:
                print('name of the extra stop left off on?')
                extraStopName = str(input())

                if os.path.exists(os.path.join('delivery', extraStopName + 'Reason.txt')) == False:
                    while True:
                        print('\nwhat was the reason for the extra stop?')

                        try:
                            extraStopReason = str(input())

                            if extraStopReason.isdigit() == False:
                                areYouSure2 = utility_function.areYouSure(extraStopReason + '.')

                                if areYouSure2 == True:
                                    utility_function.writeData("delivery", extraStopName + "Reason.txt", extraStopReason)
                                    utility_function.writeData("delivery", extraStopName + "MilesTrav.txt", milesTrav('extra'))
                                    extraEndTime = utility_function.writeData("delivery", extraStopName + "EndTime.txt", utility_function.now(), 'back')
                                    utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), extraEndTime, "extra stop")
                                    os.remove(os.path.join('delivery', 'extraStop'))

                                else:


                elif os.path.exists(os.path.join('delivery', extraStopName + 'Reason.txt')) == True and os.path.exists(os.path.join('delivery', extraStopName + 'MilesTrav.txt')) == False:
                    utility_function.writeData("delivery", extraStopName + "MilesTrav.txt", milesTrav('extra'))
                    extraEndTime = utility_function.writeData("delivery", extraStopName + "EndTime.txt", utility_function.now(), 'back')
                    utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), extraEndTime, "extra stop")
                    os.remove(os.path.join('delivery', 'extraStop'))

                else:
                    print('this extra stop does not yet exist,\nwould you like to create it?\n1 for yes | 2 for no')


        elif os.path.exists(os.path.join('delivery',


        elif os.path.exists(os.path.join('delivery', 'numbOfOrders.txt')) == True and os.path.exists(os.path.join('delivery', 'onDelivery')) == False or os.path.exists(os.path.join('delivery', 'onDelivery')) == True:

            with open(os.path.join('delivery', 'numbOfOrders.txt'), 'r') as file:
                numberOfOrder = int(file.read())

            if numberOfOrder == 1:
                onDelivery('driving to address...', datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                orderNumb = order.orderNumb()

                order.tip(orderNumb)

                milesTrav(orderNumb)

                orderEndTime = utility_function.writeData('delivery', str(orderNumb) + 'EndTime.txt', utility_function.now(), 'back')

                utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

            elif numberOfOrder >= 1:
                for value in range(numberOfOrder):
                    onDelivery('driving to address...', datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                    orderNumb = order.orderNumb()

                    order.tip(orderNumb)

                    milesTrav(orderNumb)

                    orderEndTime = utility_function.writeData('delivery', str(orderNumb) + 'EndTime.txt', utility_function.now(), 'back')

                    utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

            onDelivery('driving back to store...', datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

            milesTrav('total', 'total ')

            delivEndTime = utility_function.writeData('delivery', 'deliveryEndTime.txt', utility_function.now(), 'back')

            utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), delivEndTime, 'delivery')

            utility_function.writeData('shift', 'numbOfDeliveries.txt', int(utility_function.deliveryNumb('number')) + 1)



        elif os.path.exists(os.path.join('delivery', 'deliveryStartTime.txt')) == True and os.path.exists(os.path.join('delivery', 'numbOfOrders.txt')) == False:
            numberOfOrder = int(numbOfOrders())

            if numberOfOrder == 1:
                onDelivery('driving to address...', datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                orderNumb = order.orderNumb()

                order.tip(orderNumb)

                milesTrav(orderNumb)

                orderEndTime = utility_function.writeData('delivery', str(orderNumb) + 'EndTime.txt', utility_function.now(), 'back')

                utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

            elif numberOfOrder >= 1:
                for value in range(numberOfOrder):
                    onDelivery('driving to address...', datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                    orderNumb = order.orderNumb()

                    order.tip(orderNumb)

                    milesTrav(orderNumb)

                    orderEndTime = utility_function.writeData('delivery', str(orderNumb) + 'EndTime.txt', utility_function.now(), 'back')

                    utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

                onDelivery('driving back to store...', datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                milesTrav('total', 'total ')

                delivEndTime = utility_function.writeData('delivery', 'deliveryEndTime.txt', utility_function.now(), 'back')

                utility_function.timeTook(datetime.datetime.strptime(utility_function.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), delivEndTime, 'delivery')

                utility_function.writeData('shift', 'numbOfDeliveries.txt', int(utility_function.deliveryNumb('number')) + 1)

    else:
        pass