class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // PHASE 1 : compter les fréquences (le pattern que tu connais)
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // PHASE 2 : sortir les couples (nombre, fréquence) dans une liste
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(count.entrySet());

        // trier la liste : fréquence la plus grande en premier
        entries.sort((a, b) -> b.getValue() - a.getValue());

        // prendre les k premiers nombres
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = entries.get(i).getKey();
        }
        return result;
    }
}