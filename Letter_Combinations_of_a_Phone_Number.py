class Solution:
    # Recursive
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
                       l                         
        d = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

        self.combinations = []

        def comb(curr, i):
            if i >= len(digits):
                self.combinations.append(curr)
                return
            for letter in d[digits[i]]:
                comb(curr+letter, i+1)
            return
        
        comb("", 0)
        return self.combinations

   # Iterative
   def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        combinations = [""]
        for digit in digits:
            new_comb = []
            for combo in combinations:
                for letter in d[digit]:
                    new_comb.append(combo+letter)
            combinations = new_comb
        return combinations
