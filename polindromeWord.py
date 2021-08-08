def isPalindrome(s):
	return s == s[::-1]

s = input()
ans = isPalindrome(s)

if ans:                #controls
	print("True")
else:
	print("False")
