
# Node class that contains the name of the node, its connections, and its lowercase status.
class Node:
    def __init__(self, name, connection):
        self.name = name
        
        self.connections = []
        self.add_connection(connection)
        
        self.start = name == 'start'
        self.exit = name == 'end'
        self.small = name.islower()
        
    def add_connection(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)

# Cave class that contains all of the individual path nodes.
class Cave:
    def __init__(self, path_edges):
        self.network = {}
        self.load_network(path_edges)
        
    def load_network(self, path_edges):
        for edge in path_edges:
            edge = edge.split('-')
            for i in range(2):
                if edge[i] not in self.network.keys():
                    self.network[edge[i]] = Node(edge[i], edge[(i+1) % 2])
                else:
                    self.network[edge[i]].add_connection(edge[(i+1) % 2])
                    
    def __getitem__(self, item):
        return self.network[item]


# Read the input file              
def read_input(input):
    paths = open(input).read().strip().splitlines()
    return paths
        

# Search through the paths from the starting point
def path_search(cave, node, path, paths, double_back=False):
    path.append(node.name)
    
    # Leave the search if we've found an exit
    if node.exit:
        paths.append(path)
        return
    
    # Get the connections
    connections = node.connections
    
    # Iterate through the connections
    for connection in connections:
        new_node = cave[connection]
        # First make sure the node isn't the start
        if new_node.start:
            continue
        
        # Next make sure we haven't already visited the connection if it's small
        elif new_node.small and new_node.name in path:
            if double_back:
                smalls = [item for item in path if cave[item].small]
                two_smalls = 2 in [smalls.count(small) for small in smalls]
                if two_smalls:
                    continue
            else:
                continue
            
        # Lastly make sure we don't enter a trapped path (includes start)
        elif not double_back:
            if node.small and new_node.small and len(new_node.connections) == 1:
                continue
        
        path_search(cave, new_node, path.copy(), paths, double_back=double_back)
    
    return


def main(path_edges):
    # Build our cave map
    cave = Cave(path_edges)
    
    # Find the maximal number of paths from the 'start' node with no double backs.
    short_paths = []
    path_search(cave, cave['start'], [], short_paths)
    print (f"Number of possible short paths: {len(short_paths)}")
    
    # Find the maximal number of paths from the 'start' node for the double back configuration.
    long_paths = []
    path_search(cave, cave['start'], [], long_paths, double_back=True)
    print (f"Number of possible long paths: {len(long_paths)}")

    
if __name__ == "__main__":
    path_edges = read_input("Day 12.txt")
    main(path_edges)