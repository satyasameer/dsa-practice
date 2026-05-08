class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i+1
                tank = 0
        return start if total >=0 else -1




        # remaining_gas = 0
        # for i in range(len(gas)):
        #     if cost[i] > gas[i]:
        #         continue
        #     else:
        #         #print("starting at: ", i)
        #         start = i
        #         pos = (i + 1) % len(gas)
        #         remaining_gas = gas[i]
        #         while remaining_gas:
        #             pos = pos % len(gas)
        #             if remaining_gas - cost[pos-1] < 0:
        #                 #print("ran out of gas at pos: ", pos)
        #                 break
        #             remaining_gas += gas[pos] - cost[pos-1]
        #             #print(pos, gas[pos], cost[pos-1], remaining_gas)
        #             pos += 1
        #             if pos == start and remaining_gas - cost[pos-1] >= 0 :
        #                 #print(pos, gas[pos], cost[pos-1], remaining_gas-cost[pos-1])
        #                 return start
        # return -1