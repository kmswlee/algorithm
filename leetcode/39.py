def combinationSum(candidates, target):
    def dfs(nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
    
    ret = []
    dfs(candidates, target, [], ret)
    return ret
