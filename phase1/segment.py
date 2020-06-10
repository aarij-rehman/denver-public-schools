# Maintains the segment object. Keeps track of the prep site and carry-in sites on a segment. Also stores
# information about the timewindow which the segment must be visited and how long it takes to service the
# segment. 
class Segment: 
    prep = 0
    carry1 = 0
    carry2 = 0
    time_window = (0, 0)
    service_time = 0

    # To initalize a Segment object, you need to pass in a prep and two carry-in sites. The timewindow and 
    # service time can and should be adjusted later (You can't determine these things with just the sites). 
    def __init__(self, prep_, carry1_, carry2_):
        self.prep = prep_
        self.carry1 = carry1_
        self.carry2 = carry2_