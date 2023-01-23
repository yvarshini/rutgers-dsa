def delete_all(data, value):
    data = [x for x in data if x != value]
    return data

# 1. worst-case time complexity = O(N)
# 2. yes, the code is optimal since it uses the minimum possible time and auxillary space possible
# 3. worst-case space complexity = O(1)
# 4. best-case time-complexity is Big-Omega(N) as well