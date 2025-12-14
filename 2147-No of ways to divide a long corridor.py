class Solution(object):
    def numberOfWays(self, corridor):
        mod= 10**9+7

        total_seats = corridor.count("S")
        if total_seats < 2 or total_seats %2 != 0: 
            return 0 

        seats=0
        plants_between=0
        ways=1

        for ch in corridor:
            if ch == 'S':
                seats+=1

                if seats > 2 and seats %2 == 1:
                    ways=(ways*(plants_between+1))%mod
                    plants_between = 0

            else:
                if seats %2 ==0 and seats >=2:
                    plants_between+=1

        return ways                   
