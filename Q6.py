a = int(input())
c = 2

while c < a:
    if a % c == 0:
        print("no\n")
        break
    c += 1
if c == a:
    print("yes\n")