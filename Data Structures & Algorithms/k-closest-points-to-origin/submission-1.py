class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance= []
        hs = {}
        for point in points:
            x= point[0]
            y = point[1]
            point.append( -1*((((0 - x)**2+ (0- y)**2))**(0.5)))
        for point in points:
            distance.append([point[2],point[0],point[1]])
        heapq.heapify(distance)
        while len(distance) > k:
            heapq.heappop(distance)
        to_ret = []
        for point in distance:
            to_ret.append([point[1],point[2]])
        return to_ret