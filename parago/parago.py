# MIT License
# Copyright (c) 2019 凱(Kai)
#
# python go concurrency and R apply like parallel computation
# by Yukai Yang

import threading


def go(func, *args, **kwargs):
    """Function achieving the concurrency feature like Go language""" 

    class GoThread(threading.Thread): 

        def run(self):
            try:
                func(*args, **kwargs)
            except:
                print("Something went wrong with the function call...")
                raise

    gothread = GoThread()
    gothread.start()


def map(func, iterable, *args, **kwargs):
    """Function achieving the parallel version of the map function"""

    class MapThread(threading.Thread):

        def __init__(self, val):
            threading.Thread.__init__(self)
            self.val = val

        def run(self):
            try:
                func(self.val, *args, **kwargs)
            except:
                print("Something went wrong with the function call...")
                raise

    for val in iterable:
        mapthread = MapThread(val)
        mapthread.start()
