

def isPrime(num):
    tot=0
    for i in range(2,num):
        if(num%i) ==0 :
            tot+=1
    if tot==0 : return True

isPrime(3)

num=12
def mapReduce(num):
    m=[]
    for j in num:
        m.extend([(i,j) for i in range(2,j) if j%i==0 and isPrime(i)])
    d = {}
    for i in m:
        if d.has_key(i[0]):
            d[i[0]]+=i[1]
        else:
            d[i[0]] = i[1]
    return d
    




