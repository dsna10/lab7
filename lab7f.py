#!/usr/bin/env python3
# Student ID: dsna10

class Time:
    """Simple object type for time of the day."""
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return the sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify the current Time object by adding or subtracting seconds."""
        new_time = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def time_to_sec(self):
        """Convert the time object into total seconds from midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if the Time object is valid."""
        return (0 <= self.hour < 24) and (0 <= self.minute < 60) and (0 <= self.second < 60)

    def __str__(self):
        """Return a string representation for the object using ':'. (Used by print())"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object using '.'. (Used by interactive shell)"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Overload the '+' operator to add two Time objects."""
        return self.sum_times(t2)

def sec_to_time(seconds):
    """Convert total seconds into a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
