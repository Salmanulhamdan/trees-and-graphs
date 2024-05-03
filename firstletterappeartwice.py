def repeatedCharacter(s):
    length=len(s)
    l=list(s)
    
    dic={}

    for i in range(length-1):
        for j in range(i+1,length):
            if l[i]==l[j]:
                dic[l[i]]=j

    for i in range(length-1):
            if l[i] == l[i+1]:
                return l[i]
   
                
    return min(dic,key=lambda x : dic[x])





s="abccbaacz"
a=repeatedCharacter(s)

print(a)