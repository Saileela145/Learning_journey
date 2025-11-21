def vowels(ch):
    return ch.lower() in ['a','e','i','o','u']
def countvowls(str):
    count=0
    for i in range(len(str)):
        if vowels(str[i]):
            count+=1
    return count

str=input("enter a string:")
print("the vowels in a string",countvowls(str))
    
