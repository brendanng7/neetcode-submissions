class ValueTimePair:

    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp
    
    def __repr__(self):
        return str(self.value) + str(self.timestamp)

class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            arr = self.hashmap[key]
            arr.append(ValueTimePair(value, timestamp))
        else:
            self.hashmap[key] = [ValueTimePair(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key]
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (right + left) // 2
            valueTime = arr[mid]
            if valueTime.timestamp == timestamp:
                return valueTime.value
            elif valueTime.timestamp < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0:
            return arr[right].value
        else:
            return ""

        

        
