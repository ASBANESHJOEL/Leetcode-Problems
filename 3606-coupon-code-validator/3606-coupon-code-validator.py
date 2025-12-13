class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        valid_business = { "electronics","grocery","pharmacy","restaurant"}

        order={
            "electronics" : 0,
            "grocery" : 1,
            "pharmacy" : 2,
            "restaurant" : 3
        }

        pairs=[]

        for i in range(len(code)):
            if businessLine[i] not in valid_business:
                continue

            if not isActive[i]:
                continue

            if not code[i]:
                continue

            valid=True

            for c in code[i]:
                if not (c=="_" or c.isalnum()):
                    valid=False
                    break

            if valid:
                pairs.append((code[i],businessLine[i]))

        pairs.sort(key=lambda x:(order[x[1]],x[0]))

        res=[]

        for p in pairs:
            res.append(p[0])

        return res                  
        
        