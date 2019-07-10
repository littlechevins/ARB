class Dijkstra(g, source):

    def __init__():
        self.g = g
        self.source = source

    def start():

        dist[]
        prev[]
        Q = set()


        keys = self.g.keys()
        for key in keys:
            dist[key] = 999
            prev[key] = None
            Q.add(key)
        dist[self.source]

        while len(Q) > 0:
            u = ...
            Q.remove(u)

            for each neighbor v of u:           // only v that are still in Q
                alt = dist[u] + 1 # length(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return dist, prev
