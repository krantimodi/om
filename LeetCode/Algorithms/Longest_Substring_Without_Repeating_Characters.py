s = "abcabcbb"
s = "pwwkew"
s = "dvdf"

temp_substr_len = [''] * (len(s) + 1)

temp = list()
for n in s:
    if n in temp:
        # if a character exists, store the current substr against its length in the array
        temp_substr_len[len(temp)] = ''.join(map(str, temp))

        # remove the elements from the substr until the point where the character was repeated
        # s = "dvdf"
        pos = temp.index(n)
        del temp[0 : pos+1]

    temp.append(n)

temp_substr_len[len(temp)] = ''.join(map(str, temp))

i = len(temp_substr_len) - 1
while (i > 0):
    if temp_substr_len[i] != '':
        print (i, temp_substr_len[i])
    i -= 1

print('--neat solution---')
s = "abcabcbb"
s = "pwwkew"
s = "dvdf"

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = list(s)
        letters = {}
        if s == "":
            return 0
        if s == " ":
            return 1
        rear = 0
        front = 0
        temp = 0
        max_subset = 0
        for letter in words:
            if letter in letters and letters[letter] > rear:
                rear = letters[letter]
            front += 1
            temp = front - rear

            letters[letter] = front

            if temp > max_subset:
                max_subset = temp

        if rear == 0:
            max_subset = front
        return max_subset

class Solution:
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            if len(s) == 0:
                return 0
            last_idx = {}
            start = 0
            tmp = 0
            res = 0
            for i in range(len(s)):
                c = s[i]
                if c in last_idx and last_idx[c] >= start:
                    res = max(res, tmp)
                    start = last_idx[c] + 1
                    tmp = i - start + 1
                    last_idx[c] = i
                else:
                    last_idx[c] = i
                    tmp += 1
            return max(res, tmp)
