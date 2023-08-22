#append  ,, #extend and  #insert, #clear,#count,#pop,#remove,#reverse,#sort,#pop,#remove

l=[1,2,3,4,5]
l2=[11,12,13,14,15,16,17,18,19,20]

l.append(4545)  #append

print(l)


l.extend(l2)  #extend

print(l)

l.insert(0,100)  #insert
print(l)


cnt=l.count(11)  #count
print(cnt)


l.clear()   #clear
print(l)


l3=[1,2,3,4,5]

l3.pop()    #pop
print(l3)

l3.remove(2) #remove
print(l3)



l3.reverse()
print(l3)

l3.sort()
print(l3)