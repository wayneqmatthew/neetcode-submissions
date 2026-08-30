class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        hashmap_s = {}
        hashmap_t = {}

        ctr = 0

        if s_len == t_len:
            length = s_len
            # builds the hash map
            # initializing 0 for every letter as key
            for i in range(length):
                if s[i] not in hashmap_s:
                    hashmap_s[s[i]] = 0
                
                if t[i] not in hashmap_t:
                    hashmap_t[t[i]] = 0

            #increments 1 for every letter that shows up
            for i in range(length):
                if s[i] in hashmap_s:
                    hashmap_s[s[i]] = hashmap_s[s[i]] + 1

                if t[i] in hashmap_t:
                    hashmap_t[t[i]] = hashmap_t[t[i]] + 1

            for i in range(length):
                if (s[i] not in hashmap_t) or (t[i] not in hashmap_s):
                    return False
                else:
                    if hashmap_s[s[i]] != hashmap_t[s[i]]:
                        return False

            return True
                

        return False