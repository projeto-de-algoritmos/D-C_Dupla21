from collections import defaultdict

def longestSubstring(self, s: str, k: int) -> int:
	res = 0
	for i in range(1, 27):
		res = max(res, self.longest_substring(s, k, i))
	return res

def longest_substring(self, s, k, n) -> int:
	left, char_to_count = 0, defaultdict(int)
	res = 0
	for i in range(len(s)):
		char_to_count[ord(s[i]) - ord('a')] += 1
		while len(char_to_count) == n + 1:
			char_to_count[ord(s[left]) - ord('a')] -= 1 
			if char_to_count[ord(s[left]) - ord('a')] == 0:
				char_to_count.pop(ord(s[left]) - ord('a'))
			left += 1
		valid_count = len([_ for _ in char_to_count.values() if _ >= k])
		if len(char_to_count) == valid_count:
			res = max(res, i - left + 1)
	return res