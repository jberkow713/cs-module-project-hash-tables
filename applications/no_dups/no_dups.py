def no_dups(s):
    # Your code here
    s = s.split()
    result = []
    d = {}
    for x in s:
        if x.isspace():
            continue
        
        if x not in d:
            d[x] = 0

        d[x] +=1

    for k, v in d.items():
        result.append(k)    

    return result 


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))