import heapq

list1 = [1, 39, 2, 8, 9, 12, 99, 25, 88, 33]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3, list1))  # 最大的三个
print(heapq.nsmallest(3, list1))  # 最小的三个
print(heapq.nlargest(3, list2, key=lambda x: x['price']))
print(heapq.nsmallest(3, list2, key=lambda x: x['price']))
