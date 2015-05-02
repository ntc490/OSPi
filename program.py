#!/usr/bin/python
from weekdays import *
import datetime


class Program(object):
    def __init__(self, name="", weekdays=None, start_time=None, description=""):
        if not weekdays is None and not isinstance(weekdays, Weekdays):
            raise ValueError('weekdays need to be a weekdays.Weekdays() object')
        if not start_time is None and not isinstance(start_time, datetime.time):
            raise ValueError('start_time needs to be a datetime.time() object')
        self.name = name
        self.enabled = True
        self.weekdays = weekdays or Weekdays()
        self.start_time = start_time or datetime.time()
        self.steps = []
        self.description = description

    def is_start_datetime(self, date_and_time):
        """
        Determine if the program should trigger for the datetime object passed in
        """
        if not isinstance(date_and_time, datetime.datetime):
            raise ValueError('date_and_time needs to be of type datetime.datetime')

        if not Weekday(date_and_time.weekday()) in self.weekdays:
            return False
        if not date_and_time.time().hour == self.start_time.hour:
            return False
        if not date_and_time.time().minute == self.start_time.minute:
            return False
        return True

    def __repr__(self):
        return """
        Program name: %s
        Start time:   %s
        Weekdays:     %s
        Description:  %s
        """ % (self.name, self.start_time, str(self.weekdays), self.description)


class ProgramList(object):
    """
    List of programs that stays sorted in chronological order so testing for
    'ready' programs is as quick as possible
    """
    def __init__(self, programs=None):
        self.programs = programs or []

    def append(self, program):
        """
        Add the program to the list in sorted order
        """
        self.programs.append(program)
        # Sort list

    def delete(self, name):
        """
        Delete all programs named 'name'
        """
        for program in self.programs:
            if program.name == name:
                program_num = self.programs.index(program)
                del self.programs[program_num]

    def get_ready_program(self, datetime):
        """
        Get a reference to the first ready program in the list
        """
        for program in self.programs:
            if program.is_start_datetime(datetime) and program.enabled:
                return program
        return None

    def __len__(self):
        return len(self.programs)




# --------------- Unit Tests ---------------

if __name__ == '__main__':
    import unittest
    class ProgramTests(unittest.TestCase):
        def test(self):
            p = Program("test",
                        Weekdays(Weekday(MONDAY), Weekday(WEDNESDAY), Weekday(FRIDAY)),
                        datetime.time(hour=5, minute=0),
                        description="Test program with no instructions")
            print p
            self.assertTrue(p.is_start_datetime(datetime.datetime(year=2015, month=4, day=24, hour=5, minute=0)))
            self.assertRaises(ValueError, lambda : p.is_start_datetime("foo"))

    print "Running programs unittest"
    unittest.main()
