nw=0
while 1:
    n=int(input())
    if n==0:
        break
    best=-1
    mm=-10000
    for j in range(1,n+1):
        sm=0
        r=input()
        k=input()
        for i in range(0,len(r)):
            if(r[i]=="E"):
                break
            sm=sm+int(k[i]) if r[i]=="A" else sm
            sm=sm-int(k[i]) if r[i]=="B" else sm
            sm=sm*int(k[i]) if r[i]=="C" else sm
            sm=sm/int(k[i]) if r[i]=="D" else sm
        if sm>=mm and sm>=0:
            mm=sm
            best=j
    nw=nw+1
    if best==-1:
        print(f"Chop off!!")
    else :
        print(f"#{nw} Best :");print(f'%.4f'%mm);print(best)
    