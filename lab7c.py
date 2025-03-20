#!/usr/bin/env python3
#Author ID: epatel16

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        # Validate that the arguments are integers
        if not all(isinstance(i, int) for i in [hour, minute, second]):
            raise ValueError("Hour, minute, and second must be integers")
        
        # Further validation for valid ranges
        if not (0 <= hour < 24):
            raise ValueError("Hour must be between 0 and 23")
        if not (0 <= minute < 60):
            raise ValueError("Minute must be between 0 and 59")
        if not (0 <= second < 60):
            raise ValueError("Second must be between 0 and 59")

        self.hour = hour
        self.minute = minute
        self.second = second

def time_to_sec(time):
    '''Convert a time object to a single integer representing the number of seconds from midnight'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''Convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    '''Return a new Time object that is the sum of t1 and t2'''
    t1_sec = time_to_sec(t1)
    t2_sec = time_to_sec(t2)
    total_sec = t1_sec + t2_sec
    return sec_to_time(total_sec)

def change_time(t, seconds):
    '''Return a new Time object that is 'seconds' seconds added to t'''
    t_sec = time_to_sec(t)
    total_sec = t_sec + seconds
    return sec_to_time(total_sec)

def format_time(t):
    '''Format a Time object to a string of the form HH:MM:SS'''
    return f'{t.hour:02}:{t.minute:02}:{t.second:02}'

