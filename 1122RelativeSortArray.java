
import java.util.*;

class Solution {

    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> mapA2 = new HashMap<>();
        for (int i = 0; i < arr2.length; i++) {
            mapA2.put(arr2[i], i);
        }
        return Arrays.stream(arr1)
                .boxed()
                .sorted(Comparator.comparingInt(x -> mapA2.getOrDefault(x, arr2.length + x)))
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
