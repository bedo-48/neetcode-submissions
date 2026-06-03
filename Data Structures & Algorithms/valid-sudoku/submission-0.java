class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[] boxes = new HashSet[9];
        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char d = board[r][c];
                if (d == '.') continue;          // case vide → on saute

                int boxIndex = (r / 3) * 3 + (c / 3);

                // 1. si d est déjà dans rows[r] OU cols[c] OU boxes[boxIndex] → return false

                if(rows[r].contains(d) || cols[c].contains(d) || boxes[boxIndex].contains(d))
                {
                    return false;
                }

                // 2. sinon, ajoute d dans les trois sacs
                else
                {
                    rows[r].add(d);
                    cols[c].add(d);
                    boxes[boxIndex].add(d);

                }
            }
        }
        return true;
    }
}