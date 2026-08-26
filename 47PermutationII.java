
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        boolean[] visited = new boolean[nums.length];

        backtrack(nums, ans, new ArrayList<>(), visited);
        return ans;
    }

    private void backtrack(int[] nums, List<List<Integer>> ans, List<Integer> path, boolean[] visited) {
        if (path.size() == nums.length) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) {
                continue;
            }

            visited[i] = true;
            path.add(nums[i]);

            backtrack(nums, ans, path, visited);

            path.remove(path.size() - 1);
            visited[i] = false;
        }
    }
}
