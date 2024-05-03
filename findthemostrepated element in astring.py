string="karavansarehere"


def repeated_string(string):
    demo={}
    for i in string:
        if i in demo:
            demo[i]+=1
        else:
            demo[i]=1
    print(demo)

    max_count=0
    # repated=None

    for count in demo.values():
        if count > 1:
            max_count+=count

        

    return max_count

a=repeated_string(string)
print(a)


numbers = [-10, -20, -30, -40, -50]
max_abs_value = max(numbers, key=abs)
print(max_abs_value)


