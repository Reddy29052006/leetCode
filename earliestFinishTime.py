from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)

        minWaterEnd = min(waterStartTime[i] +
                          waterDuration[i] for i in range(m))
        minLandEnd = min(landStartTime[i] + landDuration[i] for i in range(n))

        min_land_time = float("inf")

        for j in range(m):
            min_land_time = min(min_land_time, max(
                waterStartTime[j], minLandEnd) + waterDuration[j])

        min_water_time = float("inf")
        for j in range(n):
            min_water_time = min(min_water_time, max(
                landStartTime[j], minWaterEnd) + landDuration[j])

        return min(min_land_time, min_water_time)


obj = Solution()

landStartTime = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450]
landDuration = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]

waterStartTime = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475]
waterDuration = [475, 425, 375, 325, 275, 225, 175, 125, 75, 25]


result = obj.earliestFinishTime(
    landStartTime, landDuration, waterStartTime, waterDuration)

print(result)
