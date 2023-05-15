Simple sleep timer script written in 40 lines of Python. Puts your Mac to sleep after waiting for the specified amount of time. 

**Usage**

```
usage: sleeptimer [-h] TIME_SPAN

positional arguments:
  TIME_SPAN   Time to wait before going to sleep. h = hours, m = minutes, s = seconds. For example: 1h30m

options:
  -h, --help  show this help message and exit
```

**Example**

```
>>> python3 sleeptimer.py 1h15m
Will go to sleep at [17:08:52]. Press CTRL+C to cancel.
```

**Make it easier to run**

Make the script easier to call by running `sudo python3 install.py`, which will create a shell script on PATH, so it can easily be called everywhere by just typing `sleeptimer 30m`.