strs = ["flower","flow","flight"]

res = ""
i = 0
while i < len(strs)-1:
    s = strs[i]
    r = strs[i + 1]
    for j in range(0,len(s)):
        if s[j] != r[j]:
            continue
        res += s[j]
        j += 1
    i += 1
print(res)

