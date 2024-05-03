def numDifferentIntegers( word):
    a=set()
    word = ''.join(c if c.isdigit() else ' ' for c in word)
    numbers=word.split()
    for i in numbers:
        print(i,"first")    
        i=i.lstrip('0')
        print(i)
        a.add(i)
    return len(a)

a=numDifferentIntegers("a00123bc34d0000008ef34000")

print(a)