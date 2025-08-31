class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency map of characters in the current window
        char_count = {}

        left = 0             # Left boundary of sliding window
        max_freq = 0         # Count of the most frequent character in the window
        longest = 0          # Result: length of longest valid window found

        for right in range(len(s)):  
            # Add current character (s[right]) into frequency map
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Update the maximum frequency in the current window
            max_freq = max(max_freq, char_count[s[right]])

            # Window size = right - left + 1
            # Replacements needed = window size - most frequent char count
            # If replacements exceed k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1  # move window start forward

            # Update the longest valid window size seen so far
            longest = max(longest, right - left + 1)

        return longest
