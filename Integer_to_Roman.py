class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
        res = ""
        for n, sym in vals:
            count = num // n
            if count > 0:
                res += (sym * count)
                num = num % n
        return res
