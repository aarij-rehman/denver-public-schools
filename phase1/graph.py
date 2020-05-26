# A graph class used to keep track of routes and execute the savings algorithm 
import pandas as pd
class Graph:
    segments = []
    distance = lambda: True
    routes = {}

    def __init__(self, segments, distance):
        self.segments = segments
        self.distance = distance
        for i in (range(len(segments))):
            self.routes[i] = [i]
        
    def _on_same_route(self, segment_indx1, segment_indx2):
        return segment_indx2 in self.routes[segment_indx1]
    
    def _merge_is_feasible(self, segment_indx1, segment_indx2):
        if self._on_same_route(segment_indx1, segment_indx2):
            return False
        pot_route = [ self.segments[i] for i in (self.routes[segment_indx1] + self.routes[segment_indx2]) ]
        pot_route.sort(key=lambda seg: (seg.time_window[0], seg.time_window[1]))
        return self._route_simulator(pot_route)
        
    def _route_simulator(self, route):
        current_time = pd.to_datetime('6:00 AM')
        current_location = 0
        for seg in route:
            current_time = current_time + pd.Timedelta(self.distance(current_location, seg.prep), unit="min")
            if current_time < seg.time_window[0]:
                current_time = seg.time_window[0]
            if current_time > seg.time_window[1]:
                return False
            current_time = current_time + pd.Timedelta(seg.service_time, unit="min")
            current_location = seg.prep
        return True

    def merge(self, segment_indx1, segment_indx2):
        if self._merge_is_feasible(segment_indx1, segment_indx2):
            newroute = self.routes[segment_indx1] + self.routes[segment_indx2]
            self.routes[segment_indx1] = newroute
            self.routes[segment_indx2] = newroute
            for seg_indx in newroute:
                self.routes[seg_indx] = newroute

    def get_routes(self):
        ret = []
        for i in self.routes:
            if self.routes[i] not in ret:
                ret.append(self.routes[i])
        return ret