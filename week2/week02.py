cnt = int(input("input number: "))
result = 0

# for i in range(1, cnt+1):
#     result = result + i
result = cnt * (cnt + 1) // 2 # O(1)

print(result)