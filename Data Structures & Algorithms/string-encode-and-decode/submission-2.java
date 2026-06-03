public class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for (String s : strs) {
            encoded.append(s.length());
            encoded.append("#");
            encoded.append(s);
        }

        return encoded.toString();
    }

    public List<String> decode(String encodedString) {
        List<String> result = new ArrayList<>();

        int i = 0;

        while (i < encodedString.length()) {
            int j = i;

            // Find the separator #
            while (encodedString.charAt(j) != '#') {
                j++;
            }

            // Extract the length
            int length = Integer.parseInt(encodedString.substring(i, j));

            // The string starts after #
            int start = j + 1;
            String word = encodedString.substring(start, start + length);

            result.add(word);

            // Move i to the next encoded string
            i = start + length;
        }

        return result;
    }
}