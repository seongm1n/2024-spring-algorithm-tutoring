while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    calls = []
    for _ in range(n):
        calls.append(list(map(int, input().split())))

    wiretappings = []
    for _ in range(m):
        wiretappings.append(list(map(int, input().split())))


    for start, duration in wiretappings:
        ans = 0
        for call in calls:
            if start < call[2] + call[3] and call[2] < start + duration:
                ans += 1
        print(ans)