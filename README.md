# parago
implementing the Go routine and R apply like parallel computation

# How to install

Run
```
pip install git+https://github.com/yukai-yang/parago
```
provided that pip has been installed beforehand.

# Go routine like parallel

```
# first we load the packages
import parago
import time

# define the function to test how it works
def sleep(sec):
    real = sec + offset
    print(f'Job {real} started...')
    time.sleep(real)
    print(f'Job {real} finished...')

# we need some global variable to check if the function to be forked can find it
offset = 1

# here we go!
parago.go(sleep, 2)
parago.go(sleep, 1)

# and we apply!
parago.map(sleep, range(5,1,-1))
```

The results are:

> Job 3 started...

> Job 2 started...

> Job 2 finished...

> Job 3 finished...


# R apply like parallel

```
# and we apply!
parago.map(sleep, range(5,1,-1))
```

The results are:

> Job 6 started...

> Job 5 started...

> Job 4 started...

> Job 3 started...

> Job 3 finished...

> Job 4 finished...

> Job 5 finished...

> Job 6 finished...
