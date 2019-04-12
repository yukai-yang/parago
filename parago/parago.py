# MIT License
# Copyright (c) 2019 凱(Kai)
#
# python go concurrency and R apply like parallel computation
# by Yukai Yang

import threading


def go(func, *args):
    """Function achieving the concurrency feature like Go language""" 

    class GoThread(threading.Thread): 

        def __init__(self, *args):
            threading.Thread.__init__(self)
            self.args = args

        def run(self):
            try:
                func(*self.args)
            except:
                print("Something went wrong with the function call...")
                raise

    gothread = GoThread(*args)
    gothread.start()


def map(func, iterable, *args):
    """Function achieving the parallel version of the map function"""

    class MapThread(threading.Thread):

        def __init__(self, val, *args):
            threading.Thread.__init__(self)
            self.val = val
            self.args = args

        def run(self):
            try:
                func(self.val, *self.args)
            except:
                print("Something went wrong with the function call...")
                raise

    for val in iterable:
        mapthread = MapThread(val, *args)
        mapthread.start()
