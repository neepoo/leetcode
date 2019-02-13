ARR = [3, 34, 4, 12, 5, 2]
S = 9

# 选或者不选
#       Subset(arr[5], 9)
#     ---
# 选 Sunbet(arr[4], 7)    不选 Subset(arr[4], 9)

def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr, i-1, s)
    else:
        A = rec_subset(arr, i-1, s-arr[i])
        B = rec_subset(arr, i-1, s)
        return A or B
    
print(rec_subset(ARR, len(ARR)-1, 9))
print(rec_subset(ARR, len(ARR)-1, 11))
print(rec_subset(ARR, len(ARR)-1, 12)) 