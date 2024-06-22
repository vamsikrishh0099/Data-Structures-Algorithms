class Solution {
    public List<List<String>> partition(String s) {

        List<List<String>> ans = new ArrayList<>();
        List<String> path = new ArrayList<>();

        helper2(s, 0, path, ans);
        return ans;

    }

    void helper2(String s, int start, List<String> path, List<List<String>> ans) {

        if (start == s.length()) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int i = start + 1; i <= s.length(); i++) {
            String curstring = s.substring(start, i);
            if (isPalindrome(s, start, i - 1)) {
                path.add(curstring);
                helper2(s, i, path, ans);
                path.remove(path.size() - 1);
            }
        }

    }

    void helper(String s, int index, List<String> path, List<List<String>> ans) {

        if (index == s.length()) {
            ans.add(new ArrayList<>(path));
            return;
        }
        for (int i = index; i < s.length(); i++) {
            if (isPalindrome(s, index, i)) {
                path.add(s.substring(index, i + 1));
                helper(s, i + 1, path, ans);
                path.remove(path.size() - 1);
            }
        }
    }

    boolean isPalindrome(String s, int start, int end) {
        while (start <= end) {
            if (s.charAt(start++) != s.charAt(end--))
                return false;
        }

        return true;
    }
}