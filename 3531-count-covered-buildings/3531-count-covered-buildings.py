class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        rows = {}
        cols = {}
        
        for x , y in buildings:
            rows.setdefault(y,[]).append(x)
            cols.setdefault(x,[]).append(y)

        for y in rows:
            rows[y].sort()

        for x in cols:
            cols[x].sort()

        covered = 0

        for x , y in buildings:
            row = rows[y]
            col = cols[x]  


            import bisect

            pos=bisect.bisect_left(row,x)

            left=pos>0
            right=pos<len(row)-1

            pos2=bisect.bisect_left(col,y) 

            below=pos2>0
            above=pos2<len(col)-1

            if left and right and below and above:
                covered +=1

        return covered  