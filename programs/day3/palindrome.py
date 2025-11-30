def palindrome(text):
    originaltext = text.lower().replace(" ", "")
    return originaltext == originaltext[::-1]
