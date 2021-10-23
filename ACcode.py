try:
    best=-1
    nw=0
    mm=-10000
    while 1:
        sm=0
        nw=nw+1
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
            best=nw


except:
    if best==-1:
        print("Chop off!!")
    else :
        print(f'%.4f'%mm);print(best)