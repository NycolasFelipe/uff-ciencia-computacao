xa_0, ya_0, xa_1, ya_1 = map(int, input().split())
xb_0, yb_0, xb_1, yb_1 = map(int, input().split())

if xa_0 <= xb_0 <= xa_1 or xb_0 <= xa_0 <= xb_1:
    if ya_0 <= yb_0 <= ya_1 or yb_0 <= ya_0 <= yb_1:
        print(1)
else:
    print(0)
