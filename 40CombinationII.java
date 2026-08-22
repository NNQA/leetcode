import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        
        backtrack(res, new ArrayList<>(), candidates, target, 0);
        return res;
    }
    private static void backtrack(List<List<Integer>> res, List<Integer> arr, int[] candidates, int remain, int start) {
        if (remain == 0) {
            res.add(new ArrayList<>(arr));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) {
                break;
            }
            arr.add(candidates[i]);
            backtrack(res, arr, candidates, remain - candidates[i], i);
            arr.remove(arr.size() - 1); 
        }
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};

        System.err.println(combinationSum(nums, 8));
    }
}