# MIT License
# Copyright (c) 2019 凱(Kai)
#
# python go concurrency and R apply like parallel computation
# by Yukai Yang

import threading
from functools import wraps

def go_thread(func):
    """a decorator achieving the concurrency feature like Go language"""

    @wraps(func)
    def decorated_func(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return

    return decorated_func


def map(func, iterable, *args, **kwargs):
    """a function achieving the parallel version of the map function"""

    for val in iterable:
        thread = threading.Thread(target=func, args=(val,)+args, kwargs=kwargs)
        thread.start()
