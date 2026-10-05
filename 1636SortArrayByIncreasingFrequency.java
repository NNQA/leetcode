
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

class Solution {

    public int[] frequencySort(int[] nums) {
        return Arrays.stream(nums)
                .boxed()
                .sorted(Comparator.comparingLong((Integer x) -> Arrays.stream(nums).filter(n -> n == x).count()).thenComparing(Comparator.reverseOrder()))
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
