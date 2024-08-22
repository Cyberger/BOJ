s = input()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(i+len(s))
        break