# A segment class that keeps track of a prep site with it's carry in sites
class Segment: 
    prep = 0
    carry1 = 0
    carry2 = 0
    time_window = (0, 0)
    service_time = 0

    def __init__(self, prep_, carry1_, carry2_):
        self.prep = prep_
        self.carry1 = carry1_
        self.carry2 = carry2_