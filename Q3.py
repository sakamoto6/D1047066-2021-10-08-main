print("年齡(0:<30,1:>30)")
a=int(input())
if a==1:
    print("不見")
else:
    print("長相(0:醜,1:帥,2:中等)")
    b=int(input())
    if b==0:
        print("不見")
    else:
        print("收入(0:低,1:中,2:高)")
        c=int(input())
        if c==0:
            print("不見")
        elif c==2:
            print("見")
        else:
            print("是否為公務員(0:否,1:是)")
            d=int(input())
            if d==1:
                print("見")
            else:
                print("不見")