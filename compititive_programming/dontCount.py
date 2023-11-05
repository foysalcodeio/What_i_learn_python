

def solve():
    n, m = map(int, input().split()) # take input n and m
    x = input()
    s = input()
    for i in range(6):
        if s in x:
            print(i)
            return
        x +=x
    print(-1)

#test case
for _ in range(int(input())):
    solve()
