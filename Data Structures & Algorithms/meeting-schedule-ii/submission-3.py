"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)

        meetingRooms = []
        heapq.heapify(meetingRooms)

        for i in range(len(intervals)):
            if not meetingRooms:
                heapq.heappush(meetingRooms, intervals[i].end)
            else:
                if intervals[i].start >= meetingRooms[0]:
                    heapq.heappop(meetingRooms)
                heapq.heappush(meetingRooms, intervals[i].end)
        return len(meetingRooms)                