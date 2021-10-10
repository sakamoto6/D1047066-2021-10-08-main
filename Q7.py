n = int(input(""))
if 0 < n <= 9:
    for a in range(1, n+1):
        for b in range(1, n+1):
            print(f"{a * b:2}   ", end=" ")
        print()
else:
    print("Erorr\n")