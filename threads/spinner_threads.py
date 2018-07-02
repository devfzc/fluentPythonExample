import threading
import threading
import itertools
import time
import sys

class Signal:
    status = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|\\-/'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(1)
        if not signal.status:
            break


def supervisor():
    '''
    '''
    signal = Signal()
    spinner = threading.Thread(target = spin, args = ('thinking!', signal))
    spinner.start()
    time.sleep(5)
    Signal.status = False
    

def main():
    result = supervisor()
    return result

if __name__ == '__main__':
    main()