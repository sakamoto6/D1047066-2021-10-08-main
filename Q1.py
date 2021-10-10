print("是否已有房產(0:no,1:yes)")
a=int(input())
if a==1:
    print("可貸款")
else:
    print("是否已婚(0:no,1:yes)")
    b=int(input())
    if b==1:
        print("可貸款")
    else:
        print("年收入是否>100萬(0:no,1:yes)")
        c=int(input())
        if c==1:
            print("可貸款")
        else:
            print("不可貸款")