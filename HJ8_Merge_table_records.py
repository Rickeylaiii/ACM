n = int(input().strip())
records = {}

for _ in range(n):
    x, y = map(int, input().split())
    records[x] = records.get(x, 0) + y

for key in sorted(records.keys()):
    print(key, records[key])