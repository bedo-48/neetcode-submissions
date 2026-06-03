class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;

        for (int num : set) {
            if (!set.contains(num - 1)) {            // num est un début de suite
                int current = num;
                int length = 1;
                while (set.contains(current + 1)) {  // tant que le suivant existe
                    current++;
                    length++;
                }
                longest = Math.max(longest, length); // garde le record
            }
        }

        return longest;
    }
}