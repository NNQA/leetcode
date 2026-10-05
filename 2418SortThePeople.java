
import java.util.stream.IntStream;

class Solution {

    public String[] sortPeople(String[] names, int[] heights) {
        return IntStream.range(0, names.length)
                .boxed()
                .sorted((i, j) -> Integer.compare(heights[j], heights[i]))
                .map(i -> names[i])
                .toArray(String[]::new);
    }
}
