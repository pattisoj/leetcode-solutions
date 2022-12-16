class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] %= 10
            else:
                break
        else:
            digits.insert(0, 1)
                
        return digits