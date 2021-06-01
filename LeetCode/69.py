#주어진 정수x의 제곱근구하기

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(sqrt(x))
