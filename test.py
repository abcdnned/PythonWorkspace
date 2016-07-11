dic={}
for i in range(0,10):
    dic[i]=i

l=dic.keys()
for i in range(0,100):
    if l!=dic.keys():
        print 'wrong'
        break
