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
        self.weekdays = weekdays or Weekdays()
        self.start_time = start_time or datetime.time()
        self.instructions = []
        self.description = description

    def should_trigger(self, date_and_time):
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
            self.assertTrue(p.should_trigger(datetime.datetime(year=2015, month=4, day=24, hour=5, minute=0)))
            self.assertRaises(ValueError, lambda : p.should_trigger("foo"))

    print "Running programs unittest"
    unittest.main()
