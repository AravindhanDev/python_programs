def isPalindrome(str1):
    return str1 == str1[::-1]

string = input("Enter string ")
res = isPalindrome(string)
print(res)
