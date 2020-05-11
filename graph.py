# A graph class used to keep track of routes and execute the savings algorithm 
class Graph:
    prepsites = []  # A list of the prepsites 
    arcs = set()    # A set of the arcs in the graph rn
    route = {}      # Dictionary that holds lists (adjaceny list) - 0 if two nodes are not in the same route, 1 otherwise
    depot = 0       # The school code for the depot

    def __init__(self, prep, depot):
        self.prepsites = prep
        self.arcs = set()
        self.depot = depot            
        for i in prep:
            if i != depot:
                self.arcs.add((i,depot))
                self.arcs.add((depot,i))
                self.route[i] = []

    def add_arc(self, arc):
        self.arcs.add(arc)
        newroute = list(set(self.route[arc[0]] + self.route[arc[1]] + [arc[0]] + [arc[1]]))
        self.route[arc[0]] = newroute
        self.route[arc[1]] = newroute       
        for node in newroute:
            self.route[node] = newroute
            
    def remove_arc(self, arc):
        self.arcs.remove(arc)

    def is_node_interior(self, node):
        node_depot = (node, self.depot)
        depot_node = (self.depot, node)
        return not ((node_depot in self.arcs) or (depot_node in self.arcs))

    def on_same_route(self, arc):
        return arc[1] in self.route[arc[0]]

    def is_arc_interior(self, arc):
        node1 = self.is_node_interior(arc[0])
        node2 = self.is_node_interior(arc[1])
        return (not node1) and (not node2)
    
    def merge(self, arc):
        if (arc[0],self.depot) in self.arcs:
            if (arc[1], self.depot) in self.arcs:
                self.remove_arc((arc[0], self.depot))
                self.remove_arc((arc[1], self.depot))
                self.add_arc(arc)
                return
            if (self.depot, arc[1]) in self.arcs:
                self.remove_arc((arc[0], self.depot))
                self.remove_arc((self.depot, arc[1]))
                self.add_arc(arc)
                return
        if (self.depot, arc[0]) in self.arcs:
            if (arc[1], self.depot) in self.arcs:
                self.remove_arc((self.depot, arc[0]))
                self.remove_arc((arc[1], self.depot))
                self.add_arc(arc)
                return
            if (self.depot, arc[1]) in self.arcs:
                self.remove_arc((self.depot, arc[0]))
                self.remove_arc((self.depot, arc[1]))
                self.add_arc(arc)
                return   