import time
import random

def waiting_game():
    target = random.randint(2,4)
    print('Your target time is {} seconds'.format(target))

    input('--Hit enter to start countin--')
    start_time = time.time()

    input('Hit Enter again after specified time.')

    elapsed_time = time.time() - start_time

    if elapsed_time == target:
        print('You won')
    else: print('Lost ' + str(elapsed_time))

    return

waiting_game()
