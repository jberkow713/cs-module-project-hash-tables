def word_count(s):
    # Your code here

    d = {}
    ignored = [", ",",  ",", ".",   "+", "=", "/",  
    "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    
    for c in s:
        c = s.split()
        
        if c.isspace():
            continue
        
        if c in ignored:
            continue

        c = c.lower()

        if c not in d:
            d[c] = 0

        d[c] +=1
    
    return d         

    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))