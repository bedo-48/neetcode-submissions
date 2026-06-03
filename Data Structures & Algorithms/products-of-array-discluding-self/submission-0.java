class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];

        // PASSE 1 : produits de gauche
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            // 1. écris prefix dans output[i]
            output[i] = prefix;
            // 2. fais grossir prefix avec nums[i]
            prefix = prefix * nums[i];
        }

        // PASSE 2 : produits de droite
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            // 1. multiplie output[i] par suffix
            output[i] = suffix* output[i];
            // 2. fais grossir suffix avec nums[i]
            suffix = suffix*nums[i];

        }

        return output;
    }
}