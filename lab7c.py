#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def valid_time(t):
    """Check the validity of the time object attributes"""
    return (0 <= t.hour < 24) and (0 <= t.minute < 60) and (0 <= t.second < 60)

def change_time(time, seconds):
    """Modify the time object by adding seconds"""
    new_time = sec_to_time(time_to_sec(time) + seconds)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second

def time_to_sec(time):
    """Convert time object to total seconds"""
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    """Convert total seconds to a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

