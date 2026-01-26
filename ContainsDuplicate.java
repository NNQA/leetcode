
import java.util.HashSet;




class ContainsDuplicate {
    public static Boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        
        for(int num: nums) {
            if(seen.contains(num)) {
                return true;
            } else {
                seen.add(num);
            }
        }
        return false;
        
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        System.out.println(containsDuplicate(nums));
    }
}