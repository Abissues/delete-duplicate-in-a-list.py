import collections
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
while 1:
    s=[item for item, count in collections.Counter(a).items() if count > 1]#found duplicate 
    if len(s)==0:
        print("--------------------------------------------------")
        print("compleate list without duplicate done")
        print(a)
        print("the original array len is " + str(original) + " now the len is " + str(len(a)) + " duplicate number = " + str(int(original)-(int(len(a)))))
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
