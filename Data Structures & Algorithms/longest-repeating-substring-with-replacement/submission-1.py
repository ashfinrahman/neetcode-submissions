class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # FIX: frequency map of characters in the window
        max_freq = 0        # FIX: track the highest frequency of any char in window
        l = 0
        max_count = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            # FIX: replacements needed = window size - max frequency
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            running_count = r - l + 1
            max_count = max(running_count, max_count)
        return max_count