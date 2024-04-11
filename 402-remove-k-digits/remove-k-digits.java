class Solution {
    public String removeKdigits(String num, int k) {
        if (num.length() == k) return "0";

        int[] removed = new int[num.length()];
        while (k > 0) {
            boolean foundDigitToRemove = false;
            for (int i = 0; i < num.length() - 1; i++) {
                if (removed[i] == 1) continue;

                int nextNumIndex = i + 1;
                while (nextNumIndex < num.length() && removed[nextNumIndex] == 1) {
                    nextNumIndex++;
                }
                if (nextNumIndex == num.length()) break;

                if (Character.getNumericValue(num.charAt(i)) > Character.getNumericValue(num.charAt(nextNumIndex))) {
                    removed[i] = 1;
                    k--;
                    foundDigitToRemove = true;
                    break; // Break after removing a digit
                }
            }
            // If no digit was removed in the pass, remove from the end
            if (!foundDigitToRemove) {
                for (int i = num.length() - 1; i >= 0 && k > 0; i--) {
                    if (removed[i] == 0) {
                        removed[i] = 1;
                        k--;
                    }
                }
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < num.length(); i++) {
            if (removed[i] == 0) {
                ans.append(num.charAt(i));
            }
        }
        while (ans.length() > 1 && ans.charAt(0) == '0') {
            ans.deleteCharAt(0); // Remove leading zeros
        }
        
        return ans.length() == 0 ? "0" : ans.toString();
    }
}
