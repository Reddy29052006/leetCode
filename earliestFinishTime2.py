from typing import List


def finishAfterTwoRides(firstStart, firstDur, secondStart, secondDur):
    firstEnd = float("inf")

    for start, dur in zip(firstStart, firstDur):
        firstEnd = min(firstEnd, start + dur)

    totalEnd = float("inf")

    for start, dur in zip(secondStart, secondDur):
        end = max(start, firstEnd) + dur
        totalEnd = min(totalEnd, end)

    return totalEnd


class Solution:
    def earliestFinishTime(self,  landStartTime: List[int],  landDuration: List[int],  waterStartTime: List[int],  waterDuration: List[int]) -> int:

        return min(finishAfterTwoRides(landStartTime, landDuration, waterStartTime, waterDuration),
                   finishAfterTwoRides(waterStartTime, waterDuration, landStartTime, landDuration))
