class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed) ]
        pairs.sort(reverse = True)  # sorting this ensures, we start to look at cars from closer to the target

        # if speed of the current car is greater than the one seen before, it'll join the fleet, don't append as a new fleet
        # in all other cases, append
        stack = []
        for p, s in pairs:
            time = (target-p)/s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
                