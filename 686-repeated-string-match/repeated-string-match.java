class Solution {
    public int repeatedStringMatch(String a, String b) {
        StringBuilder sb = new StringBuilder(a);
        int count = 1;
        
        // Ensure sb is longer than b or at least until b can be a substring of the repeated a.
        while (sb.length() < b.length()) {
            sb.append(a);
            count++;
        }
        
        // If b is a substring of the current sb, return count.
        if (sb.toString().contains(b)) {
            return count;
        }
        
        // Append once more because b might start at the end of the first repetition of a.
        sb.append(a);
        count++;
        
        if (sb.toString().contains(b)) {
            return count;
        }
        
        // If none of the conditions are met, b cannot be a substring of any repetition of a.
        return -1;
    }
}
