import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        
        avg_speed = float(sum(dist)) / hour
        if avg_speed <= 1:
            return 1
        
        min_speed = int(avg_speed)
        max_speed = max(dist) * 100 + 1
        speed = -1
        
        while min_speed < max_speed:      
            speed = (min_speed + max_speed) // 2
            travel_time = self.calculate_travel_time(dist, speed)
            if travel_time <= hour:
                max_speed = speed
            else:
                min_speed = speed + 1

        if min_speed == max_speed:
            return min_speed 
        else:
            return speed
        
    def calculate_travel_time(self, dist, speed):
        travel_time = 0
        for d in dist:
            travel_time = math.ceil(travel_time) + d/speed
        return travel_time
        
