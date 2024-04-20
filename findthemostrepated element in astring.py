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
    repated=None

    for ch, count in demo.items():
        if count > max_count:
            max_count=count
            repated=ch

        

    return repated

a=repeated_string(string)
print(a)


# numbers = [-10, -20, -30, -40, -50]
# max_abs_value = max(numbers, key=abs)
# print(max_abs_value)