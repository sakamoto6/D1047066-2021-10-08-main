a=int(input())
if a%400==0:
    print("閏年")
elif a%100==0:
    print("平年,離a最近的閏年是",a-4,"和",a+4)    
elif a%4==0:
    print("閏年")
else:
    print("平年")
    if a%4 ==1:
        print("離a最近的閏年是",a-1)
    elif a%4 ==2:
        print("離a最近的閏年是",a-2,"和",a+2)
    elif a%4 ==3:
        print("離a最近的閏年是",a+1)