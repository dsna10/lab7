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
    sum_time = Time(0, 0, 0)
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second

    # Carry over if seconds or minutes exceed 60
    if sum_time.second >= 60:
        sum_time.second -= 60
        sum_time.minute += 1
    if sum_time.minute >= 60:
        sum_time.minute -= 60
        sum_time.hour += 1

    return sum_time

def valid_time(t):
    """Check the validity of the time object attributes"""
    return (0 <= t.hour < 24) and (0 <= t.minute < 60) and (0 <= t.second < 60)

def change_time(time, seconds):
    """Modify the time object by adding seconds"""
    time.second += seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
