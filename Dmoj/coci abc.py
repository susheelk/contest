lst = [0, 0, 0]
nums = map(int, raw_input().split())
string = raw_input()
for i in range(len(string)):
    if string[i] == "A":
        lst[i] = min(nums)
    elif string[i] == "C":
        lst[i] = max(nums)
    else:
        b = nums[:]
        b.remove(max(b))
        b.remove(min(b))
        lst[i] = b[0]

print ''.join(map(str, lst))
