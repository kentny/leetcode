# https://leetcode.com/problems/time-based-key-value-store/description/


# class ValueTimestamp:
#     def __init__(self, value: str, timestamp: int):
#         self.value = value
#         self.timestamp = timestamp


class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        index = self.search(key, timestamp)
        if index is None:
            if key in self.map:
                self.map[key].insert(0, (value, timestamp))
            else:
                self.map[key] = [(value, timestamp)]
        else:
            self.map[key].insert(index + 1, (value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        index = self.search(key, timestamp)
        if index is None:
            return ""

        return self.map[key][index][0]

    def search(self, key: str, timestamp: int) -> int | None:
        if key in self.map:
            value_timestamp_list = self.map[key]
        else:
            return None

        left = 0
        right = len(value_timestamp_list) - 1
        result = None

        while left <= right:
            mid = int((left + right) / 2)
            mid_timestamp = value_timestamp_list[mid][1]
            if mid_timestamp == timestamp:
                return mid
            if timestamp < mid_timestamp:
                right = mid - 1
            elif mid_timestamp < timestamp:
                left = mid + 1
                result = mid

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
