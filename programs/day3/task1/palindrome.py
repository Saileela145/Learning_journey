def palindrome(text):
    originaltext=text.lower().replace(" ","")
    return originaltext==originaltext[::-1]
word="Madam"
if palindrome(word):
    
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")


num=123321
if palindrome(str(num)):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
          

          
          
