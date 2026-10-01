class Solution:
    def destCity(self, paths: list[list[str]]) -> str:

        mapDest = {}
        mapStart = {}

        for path in paths:
            start, dest = path[0], path[1]
            mapDest[dest] = mapDest.get(dest, 0) + 1
            mapStart[start] = mapStart.get(start, 0) + 1

        for dest in mapDest:
            if dest not in mapStart:
                return dest
        return ""
