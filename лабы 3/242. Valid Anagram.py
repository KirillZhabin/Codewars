class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_map={}
        t_map={}

        for i in range(len(s)):
            s_map[s[i]]=s_map.get(s[i],0)+1
            t_map[t[i]]=t_map.get(t[i],0)+1
        if len(s_map)!=len(t_map):
            return False
        for item in (s_map):
            if(s_map[item]!=t_map.get(item,0)):
                return False
        return True