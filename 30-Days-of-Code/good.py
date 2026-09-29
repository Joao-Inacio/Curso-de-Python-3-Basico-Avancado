k = 2
nums = [1,3,2,1,5,4]
for i, n in enumerate(nums):
    k_menos = i - k
    k_mais = i + k
    if k_menos > k or k_mais < k:
        print(i, i)

