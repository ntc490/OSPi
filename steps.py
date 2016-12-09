# Maybe "steps" can be of different types: Turning on and then off, turning "on"
# only, or turning "off" only?
ACTION_TYPE_ON_OFF = 1
ACTION_TYPE_ON = 2
ACTION_TYPE_OFF = 3



class Step(object):
    """
    A step is an action within a program
    """
    def __init__(self, stations=None, duration=0, type=ACTION_TYPE_ON_OFF):
        self.stations = stations or []
        self.duration = duration
        self.type = type
        self.expiration = None

    def start(self, current_time):
        self.expiration = current_time + self.duration

    def is_done(self, current_time):
        if self.expiration and current_time >= self.expiration:
            return True
        else:
            return False

    def __repr__(self):
        return "%s for %d seconds" % (self.stations, self.duration)
