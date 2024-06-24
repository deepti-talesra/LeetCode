class Solution:
    # Recursive/Back-tracking approach
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def comb(curr, start, target):
            if target == 0:
                result.append(curr)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                comb(curr + [candidates[i]], i, target - candidates[i])
            return
        
        comb([], 0, target)
        return result

  # Dynamic Programming approach
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      result = [[] for _ in range(target+1)]
      result[0] = [[]]
      for cand in candidates:
          for i in range(cand, target+1):
              for comb in result[i-cand]:
                  result[i].append(comb + [cand])
      return result[target]
