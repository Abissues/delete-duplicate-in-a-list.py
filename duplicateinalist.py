import collections
import time
import os
scelta=int(input("1-per inserire manualmente\n 2-per scegliere un file "))
if scelta==1:
    #the duplicate start delete from end
    a=[]#your lis
    maxleaght=int(input("how many value did you want  "))#len of your list
    count=0#count value insert
    while maxleaght!=0:
        x=input("give me the value you actualy insert = " + str(count) + " value " )#add your values
        if len(x)==0:#if is Null
            print("you didn't add any value, dont'add anithing i will give you a new value to add ")
            maxleaght+=1
            count-=1#resent counter
        else:
            a.append(x)#add element
        maxleaght-=1
        count+=1
    original=len(a)
    start_time = time.time()
    while 1:
        s=[item for item, count in collections.Counter(a).items() if count > 1]#found duplicate 
        if len(s)==0:
            print("--------------------------------------------------")
            print("compleate list without duplicate done")
            print(a)
            print("the original array len is " + str(original) + " now the len is " + str(len(a)) + " duplicate number = " + str(int(original)-(int(len(a)))))
            print("--- %s seconds ---" % (time.time() - start_time))
            break
        else:
            print("--------------------------------------------------")
            print("list of duplicate ", s)#print all duplicate list version
            print("now printing without list")
            extract=0
            a.reverse()
            while len(s)-1>=extract:
                print(s[extract],end=" ")#print duplicate string version
                a.remove(s[extract])#remove duplicate from original list
                extract+=1
        a.reverse()
        print("\n"+"list without duplicate ",a)#original list without duplicate
else:
    nome=input("nome del file  ")
    try:
        p=open(nome,"r")
        a=p.readlines()
        p.close()
        original=len(a)
        start_time = time.time()
        while 1:
            s=[item for item, count in collections.Counter(a).items() if count > 1]#found duplicate 
            if len(s)==0:
                print("--------------------------------------------------")
                print("compleate list without duplicate done")
                print(a)
                print("the original array len is " + str(original) + " now the len is " + str(len(a)) + " duplicate number = " + str(int(original)-(int(len(a)))))
                print("--- %s seconds ---" % (time.time() - start_time))
                salvare=int(input("inserire 1 per salvare in un nuovo file tutte le parole senza duplicati "))
                if salvare == 1:
                    nuovofile=input("dammi il nome verrà salvato in .txt ")
                    x=open(nuovofile+".txt",'w+')
                    x.close()
                    x=open(nuovofile+".txt",'a')
                    for ele in a:
                        p=x.write(ele)
                    x.close()
                else:
                    pass   
                break
            else:
                print("--------------------------------------------------")
                print("list of duplicate ", s)#print all duplicate list version
                print("now printing without list")
                extract=0
                a.reverse()
                while len(s)-1>=extract:
                    print(s[extract],end=" ")#print duplicate string version
                    a.remove(s[extract])#remove duplicate from original list
                    extract+=1
            a.reverse()
            print("\n"+"list without duplicate ",a)#original list without duplicate
        input("done")
    except:
        print("nome del file inesistente riavvio in corso ")
        os.system("duplicateinalist.py")
        
