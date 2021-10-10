n = int(input(""))
a = 1
if n <= 20:
    for i in range(1, n+1):
        a = a * i
    print(a, "\n") 
else:
    print("Erorr\n")
