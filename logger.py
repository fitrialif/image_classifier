import sys
import time, datetime
import itertools

LOG_FILE = 'logs/info_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"

#- Helpers

def write_to_file(txt):
    with open(LOG_FILE, "a") as log:
        log.write(str(txt))

def log_level_in_tab(lvl):
    s = ""
    if lvl == 0:
        return s
    else:
        for _ in itertools.repeat(None, lvl):
            s += "\t"
    return s

def seconds_to_time_string(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def datetime_difference_in_time_string(x, y):
    delta = y-x
    seconds = divmod(elapsedTime.total_seconds(), 60)
    return seconds_to_time_string(seconds)

#- Public functions

def header():
    s = "---------------------------------------------------------------------\n"
    s += "----New training started the " + str(datetime.datetime.now()) + "----\n"
    s += "---------------------------------------------------------------------\n"
    write_to_file(s)

def log(txt, lvl=0):
    write_to_file(log_level_in_tab(lvl) + txt + "\n")

def execution_time(start_time, title, lvl=0):
    end_time = time.time()
    seconds = end_time - start_time
    s = title + " : executed in " + seconds_to_time_string(seconds)
    log(s, lvl)


def footer(start_datetime):
    total_time = datetime_difference_in_time_string(start_datetime, datetime.datetime.now())
    s = "Script executed in " + total_time
    s += "\n---------------------------------------------------------------------\n"
    s += "---------------------------------------------------------------------\n\n"
    write_to_file(s)
