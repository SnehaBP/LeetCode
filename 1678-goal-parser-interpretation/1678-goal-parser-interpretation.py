class Solution:
    def interpret(self, command: str) -> str:
        string=""
        i=0
        while i<len(command):
            if command[i]=="G":
                string=string+"G"
                i+=1
            elif command[i:i+2]=="()":
                string=string+"o"
                i+=1
            elif command[i:i+4]=="(al)":
                string=string+"al"
                i+=4
            else:
                i+=1
        return string