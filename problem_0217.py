class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numbers_seen = set()
        
        for number in nums:
            if number in numbers_seen:
                return True
            else:
                numbers_seen.add(number)
        
        return False