class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length())
        {
            return false;

        }

        int[] count = new int[26];

        for (int i = 0 ; i<s.length() ; i++)
        {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i)-'a']--;

        }

        for (int number = 0; number<count.length; number ++)
        {
            if(count[number]!=0){
                return false;
            }
        }

        return true;

    }
}
