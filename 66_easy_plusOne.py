class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        i = len(digits)
        digits[i - 1] += 1
        carry = 0
        while i > 0:
            i -= 1
            num = digits[i] + carry
            carry = int(num / 10)
            digits[i] = int(num % 10)
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits
