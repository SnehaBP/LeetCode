class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        integer=0
        i=0
        while i<len(s)-1:
            if roman[s[i]]<roman[s[i+1]]:
                integer+=roman[s[i+1]]-roman[s[i]]
                i+=1
            else:
                integer+=roman[s[i]]
            i+=1
        if i!=len(s):
            integer+=roman[s[-1]]
        return integer