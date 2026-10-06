import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
class Solution() {
    public int[] topKFrequent(int[] nums, int k){
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = 
            new PriorityQueue<>((a,b) -> Integer.aompare(a.getValue(), b.getValue()))

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] result = new int[k];
        int index = 0;
        while (!minHeap.isEmpty()) {
            result[index++] = minHeap.poll().getKey();
        }

        return result;
    }
}