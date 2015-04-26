#!/usr/bin/python
import sets


# Using these constants allows python to check args
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6



class Weekday(object):
    """
    Day of the week class.  Can only be set to a valid day of the week using
    numeric values MONDAY .. FRIDAY or with the day name (case-insensitive).
    """
    day_map = { MONDAY    : "Monday",
                TUESDAY   : "Tuesday",
                WEDNESDAY : "Wednesday",
                THURSDAY  : "Thursday",
                FRIDAY    : "Friday",
                SATURDAY  : "Saturday",
                SUNDAY    : "Sunday" }

    def __init__(self, day=None):
        self.day = MONDAY
        if not day is None:
            self.set(day)

    def set(self, day):
        """
        Set the day using numeric constant MONDAY ... SUNDAY or strings.
        Matching of strings is case insensitive.
        """
        if day in Weekday.day_map.keys():
            self.day = day
        elif str(day).upper() in [d.upper() for d in Weekday.day_map.values()]:
            for day_num,day_name in Weekday.day_map.items():
                if day.upper() == day_name.upper():
                    self.day = day_num
                    break
        else:
            raise ValueError('invalid day %s' % day)

    def num(self):
        "Return the day number"
        return self.day

    def __eq__(self, other):
        "Overload == operator"
        return self.day == other.day

    def __repr__(self):
        "String representation is the name of the day from day_map"
        return "%s" % Weekday.day_map[self.day]


class Weekdays(object):
    """
    Keeps a set of weekday objects
    """
    def __init__(self, *weekdays):
        """
        Create an object with an optional set of Weekday objects
        """
        self.days = sets.Set()
        for day in weekdays:
            self.add(day)

    def update(self, weekdays):
        "Add weekdays to set"
        self.days.update(weekdays.days)

    def add(self, weekday):
        "Add weekday to set"
        if not isinstance(weekday, Weekday):
            raise ValueError('Non Weekday argument invalid')
        self.days.add(weekday.day)

    def remove(self, weekday):
        "Remove weekday from set.  Raise KeyError if not present."
        if not isinstance(weekday, Weekday):
            raise ValueError('Non Weekday argument invalid')
        self.days.remove(weekday.day)

    def clear(self):
        "Remove all days from set"
        self.days.clear()

    def intersection_update(self, t):
        "Keep intersection of self and t"
        self.days.intersection_update(t.days)

    def difference_update(self, t):
        "Keep self - t"
        self.days.difference_update(t.days)

    def __len__(self):
        return len(self.days)

    def __iter__(self):
        for day_num in self.days:
            yield Weekday(day_num)

    def __contains__(self, weekday):
        "Overload 'in' operator"
        return weekday.day in self.days

    def __repr__(self):
        "Comma separated concatendation of all days in the collection"
        return ", ".join([Weekday.day_map[day] for day in self.days])




# --------------- Unit Tests ---------------

if __name__ == '__main__':
    import unittest
    class WeekdayTests(unittest.TestCase):
        def test(self):
            for day_name in Weekday.day_map.values():
                print "Create a weekday object for %s -> %s" % (day_name, Weekday(day_name))
                self.assertTrue(day_name == str(Weekday(day_name.lower())))

            for day_num in Weekday.day_map.keys():
                new_day = Weekday(day_num)
                print "Create a weekday object for %d -> %s" % (day_num, new_day)
                self.assertTrue(new_day.num() == day_num)

            print "Make sure we raise an exception for the wrong day name"
            self.assertRaises(ValueError, lambda : Weekday("invalid day"))

            print "Make sure we raise an exception for the wrong day number"
            self.assertRaises(ValueError, lambda : Weekday(-1))

            print "Make sure we raise an exception for the wrong day number"
            self.assertRaises(ValueError, lambda : Weekday(7))


    class WeekdaysTests(unittest.TestCase):
        def test(self):
            monday = Weekday(MONDAY)
            tuesday = Weekday(TUESDAY)
            second_tuesday = Weekday(TUESDAY)
            wednesday = Weekday(WEDNESDAY)
            thursday = Weekday(THURSDAY)
            friday = Weekday(FRIDAY)

            s = Weekdays()
            s.add(monday)
            print "Test for day membership"
            self.assertTrue(monday in s)
            print "Make sure tuesday doesn't exist yet"
            self.assertFalse(tuesday in s)

            s.add(tuesday)
            print "Make sure tuesday was added"
            self.assertTrue(tuesday in s)

            print "Make sure we can create sets with multiple entries"
            s = Weekdays(monday, tuesday, wednesday)
            self.assertTrue(monday in s)
            self.assertTrue(tuesday in s)
            self.assertTrue(wednesday in s)

            print "Make sure the len() function works"
            self.assertTrue(len(s), 3)

            print "Make sure monday is properly removed"
            s.remove(monday)
            self.assertFalse(monday in s)

            s.add(monday)
            s.add(thursday)
            s.add(friday)

            n = Weekdays(monday, wednesday)
            s.difference_update(n)
            print "Checking difference update"
            self.assertFalse(monday in s)
            self.assertTrue(tuesday in s)
            self.assertFalse(wednesday in s)
            self.assertTrue(thursday in s)
            self.assertTrue(friday in s)
            self.assertTrue(len(s), 3)

            print "Make sure we can do an intersection, too"
            s.update(n)
            self.assertTrue(len(s), 5)
            s.intersection_update(n)
            self.assertTrue(len(s), 3)

    print "Running weekdays unittest"
    unittest.main()
