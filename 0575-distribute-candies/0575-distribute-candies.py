class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = {}

        for i in range(0, len(candyType)):
            if candyType[i] in d:
                d[candyType[i]] += 1
            else:
                d[candyType[i]] = 1

        n = len(candyType)
        allowed_candy = n//2
        print(allowed_candy)
        
        all_candy_type = len(d.values())
        print(all_candy_type)
        
        if allowed_candy == all_candy_type:
            return all_candy_type
        elif allowed_candy > all_candy_type:
            return all_candy_type
        elif allowed_candy < all_candy_type:
            return allowed_candy
         

        