from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            print(asteroid, "    ", mass)
            if asteroid <= mass:
                mass += asteroid
            else:
                return False
        return True


obj = Solution()

mass = 5
asteroids = [4, 9, 23, 4]

result = obj.asteroidsDestroyed(mass, asteroids)

print(result)
