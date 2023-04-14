def getPrefixScores(arr):
  ans, n = [], len(arr)
  pre, pre_sum, pre_max = [0] * n, [0] * n, [0] * n
  pre[0], pre_sum[0], pre_max[0] = arr[0], arr[0], arr[0]
  for i in range(1, n):
  pre[i] = pre[i - 1] + arr[i]
  pre_sum[i] = pre_sum[i - 1] + pre[i]
  pre_max[i] = max(pre_max[i - 1], arr[i])
  for i in range(n):
  ans.append((pre_sum[i] + (i + 1) * pre_max[i]) % (10 ** 9 + 7))
return ans
